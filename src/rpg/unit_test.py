import unittest
from unittest.mock import patch
from io import StringIO
from contextlib import redirect_stdout
from test.support import captured_stdout
import sys


from RPG import Character, Player, HealingItem, AttackItem, RecoveryAgents, Bom, EnemyManager, Enemy, Goblin, Orc, Slime, get_valid_input, choose_item, reset_game, print_status, main


class CharacterTestCase(unittest.TestCase):
    def setUp(self):
        # テストの前準備を行う
        self.character = Character("勇者", 100, 20, 10)

    def tearDown(self):
        # テストの後始末を行う
        self.character = None

    def test_character_name(self):
        self.assertEqual(self.character.name, "勇者", "キャラクターの名前が正しいこと")

    def test_character_health(self):
        self.assertEqual(self.character.health, 100, "キャラクターの体力が正しいこと")

    def test_character_mp(self):
        self.assertEqual(self.character.mp, 20, "キャラクターの魔力が正しいこと")

    def test_character_attack_damage(self):
        self.assertEqual(self.character.attack_damage, 10, "キャラクターの攻撃力が正しいこと")

    def test_character_attack(self):
        target = Character("敵", 50, 10, 10)

        with captured_stdout() as stdout:
            self.character.attack(target)
            result = [
                50 - damage for damage in range(1, self.character.attack_damage + 1)]
            self.assertIn(target.health, result, "攻撃によって敵の体力が減少すること")

            expected_output = f'勇者の攻撃！ 敵に{50 - target.health}のダメージ！\n'
            self.assertEqual(stdout.getvalue(),
                             expected_output, "攻撃力の出力が正しいこと")


class PlayerTestCase(unittest.TestCase):
    def setUp(self):
        # テストの前準備を行う
        self.player = Player("勇者", 100, 20, 10)
        self.exp = pow(self.player.level, 2) * 10
        self.recovery_item = RecoveryAgents()
        self.attack_item = Bom()
        self.enemy = Goblin()

    def tearDown(self):
        # テストの後始末を行う
        self.player = None
        self.exp = None
        self.recovery_item = None
        self.attack_item = None
        self.enemy = None

    def test_player_initial_level(self):
        self.assertEqual(self.player.level, 1, "プレイヤーの初期レベルが1であること")

    def test_player_initial_exp(self):
        self.assertEqual(self.player.exp, 0, "プレイヤーの初期経験値が0であること")

    def test_max_health(self):
        self.assertEqual(self.player.max_health, 100, "プレイヤーの最大体力が正しいこと")

    def test_max_mp(self):
        self.assertEqual(self.player.max_mp, 20, "プレイヤーの最大魔力が正しいこと")

    def test_initial_items_is_none(self):
        self.assertEqual(self.player.items, list(), "プレイヤーの初期アイテムリストが空であること")

    def test_level_up(self):
        expected_level = self.player.level + 1
        expected_max_health = self.player.max_health + 10
        expected_output = f'{self.player.name}はレベル{expected_level}にアップした！ HPが回復した！\n'

        with captured_stdout() as stdout:
            self.player.level_up()

            self.assertEqual(self.player.level, expected_level,
                             "プレイヤーのレベルが正しくアップされること")
            self.assertEqual(self.player.max_health,
                             expected_max_health, "プレイヤーの最大体力が正しく増加すること")
            self.assertEqual(stdout.getvalue(),
                             expected_output, "レベルアップ時の出力が正しいこと")

    def test_gain_exp(self):
        self.player.gain_exp(1)

        self.assertEqual(self.player.exp, 1, "プレイヤーの経験値が正しく増加すること")

        # 標準出力を表示させないため
        with captured_stdout() as stdout:
            self.player.gain_exp(self.exp)

            self.assertEqual(self.player.exp, 0, "プレイヤーの経験値がリセットされること")

    def test_use_recovery_item(self):
        self.player.add_item(self.recovery_item)
        # ダメージを想定
        self.player.health -= 50

        except_health = min(
            self.player.max_health, self.player.health + self.recovery_item.restore_amount)
        except_output = f"{self.player.name}は{self.recovery_item.name}を使って{self.recovery_item.restore_amount}のHPを回復した！\n"

        with captured_stdout() as stdout:
            self.player.use_item(self.recovery_item, target=None)

            self.assertEqual(self.player.health,
                             except_health, "プレイヤーの体力が正しく回復すること")
            self.assertEqual(stdout.getvalue(), except_output,
                             "回復アイテム使用時の出力が正しいこと")
            self.assertNotIn(self.recovery_item, self.player.items,
                             "プレイヤーのアイテムリストからアイテムが削除されること")

    def test_use_attack_item(self):
        self.player.add_item(self.attack_item)

        except_enemy_health = self.enemy.health - self.attack_item.attack_damage
        except_output = f"{self.player.name}は{self.attack_item.name}を使って{self.enemy.name}に{self.attack_item.attack_damage}のダメージを与えた！\n"

        with captured_stdout() as stdout:
            self.player.use_item(self.attack_item, target=self.enemy)

            self.assertEqual(self.enemy.health,
                             except_enemy_health, "敵の体力が正しく減少すること")
            self.assertEqual(stdout.getvalue(), except_output,
                             "攻撃アイテムの使用時の出力が正しいこと")
            self.assertNotIn(self.attack_item, self.player.items,
                             "プレイヤーのアイテムリストからアイテムが削除されること")

    def test_add_item(self):
        self.player.add_item(self.recovery_item)

        self.assertIn(self.recovery_item, self.player.items,
                      "アイテムがプレイヤーのアイテムリストに追加されること")
        self.assertNotIn(self.attack_item, self.player.items,
                         "別のアイテムはプレイヤーのアイテムリストに含まれないこと")


class EnemyTestCase(unittest.TestCase):
    def setUp(self):
        # test の前準備をする
        self.enemy = Enemy(
            name="ゴブリン",
            health=30,
            mp=5,
            attack_damage=8,
            exp_reward=15)

    def tearDown(self):
        # テストの後始末を行う
        self.enemy = None

    def test_enemy_exp_rewards(self):
        self.assertEqual(self.enemy.exp_reward, 15, "敵の経験値が正しいこと")


class HealingItemTestCase(unittest.TestCase):
    def setUp(self):
        self.Item = HealingItem(
            name="アイテム", description="説明", restore_amount=20)

    def tearDown(self):
        self.item = None

    def test_item_name(self):
        self.assertEqual(self.Item.name, "アイテム", "回復アイテムの名前が正しいこと")

    def test_item_description(self):
        self.assertEqual(self.Item.description, "説明", "回復アイテムの説明が正しいこと")

    def test_restore_amount(self):
        self.assertEqual(self.Item.restore_amount, 20, "回復アイテムの回復量が正しいこと")

    def test_kind(self):
        self.assertEqual(self.Item.kind, "回復", "回復アイテムの種類が正しいこと")


class AttackItemTestCase(unittest.TestCase):
    def setUp(self):
        self.Item = AttackItem(
            name="アイテム", description="説明", attack_damage=50)

    def tearDown(self):
        self.item = None

    def test_item_name(self):
        self.assertEqual(self.Item.name, "アイテム", "攻撃アイテムの名前が正しいこと")

    def test_item_description(self):
        self.assertEqual(self.Item.description, "説明", "攻撃アイテムの説明が正しいこと")

    def test_restore_amount(self):
        self.assertEqual(self.Item.attack_damage, 50, "攻撃アイテムの攻撃力が正しいこと")

    def test_kind(self):
        self.assertEqual(self.Item.kind, "攻撃", "攻撃アイテムの種類が正しいこと")


class EnemyManagerTestCase(unittest.TestCase):
    def setUp(self):
        self.enemy_manager = EnemyManager()

    def tearDown(self):
        self.enemy_manager = None

    def test_add_enemy(self):
        enemy = Goblin()
        self.enemy_manager.add_enemy(enemy)

        self.assertIn(enemy, self.enemy_manager.enemies, "敵が正しく追加されていること")

    def test_next_enemy_with_enemies(self):
        goblin = Goblin()
        orc = Orc()
        slime = Slime()

        self.enemy_manager.add_enemy(goblin)
        self.enemy_manager.add_enemy(orc)
        self.enemy_manager.add_enemy(slime)

        with captured_stdout() as stdout:
            self.enemy_manager.next_enemy()

            self.assertEqual(self.enemy_manager.current_enemy,
                             goblin, "敵が正しく設定されていること")
            self.assertNotIn(
                goblin, self.enemy_manager.enemies, "リストから敵だ取り除かれていること")
            self.assertEqual(stdout.getvalue(),
                             f"{goblin.name}が現れた！\n", "正しいメッセージが追加されていること")

    def test_next_enemy_without_enemies(self):
        with captured_stdout() as stdout:
            self.enemy_manager.next_enemy()

            self.assertIsNone(self.enemy_manager.current_enemy,
                              "敵がいない時Noneが設定されていること")
            self.assertEqual(stdout.getvalue(), "", "出力メッセージがないこと")

    def test_reset(self):
        self.enemy_manager.add_enemy(Goblin())
        self.enemy_manager.add_enemy(Orc())
        self.enemy_manager.add_enemy(Slime())

        with captured_stdout() as stdout:
            self.enemy_manager.next_enemy()  # リストから敵を取り出す

            self.enemy_manager.reset()

            self.assertEqual(len(self.enemy_manager.enemies),
                             3, "敵リストが正しく初期化されていること")
            self.assertIsNone(self.enemy_manager.current_enemy,
                              "現在の敵がNoneにリセットされていること")

    def test_is_defeated_with_enemies(self):
        self.enemy_manager.add_enemy(Goblin())
        self.enemy_manager.add_enemy(Orc())
        self.enemy_manager.add_enemy(Slime())

        self.assertFalse(self.enemy_manager.is_defeated(),
                         "敵がいる場合はFalseが返されること")

    def test_is_defeated_without_enemies(self):
        self.assertTrue(self.enemy_manager.is_defeated(),
                        "敵がいない場合はTrueが返されること")


class UtilityRPGTestCase(unittest.TestCase):
    @unittest.skip("無限ループから抜けなくなるため、手動でテストする")
    @patch('builtins.input', side_effect=['2'])
    def test_get_valid_input(self, mock_input):
        expected_output = "無効な選択です。再度入力してください。\n選択肢を入力してください: "
        mock_input.__iter__.return_value = ['2']

        stdout = StringIO()

        # with redirect_stdout(StringIO()) as stdout:
        with patch('sys.stdout', stdout):
            choice = get_valid_input(["1", "3", "5"])

        self.assertEqual(choice, "2", "正しい選択が返されること")
        self.assertEqual(stdout.getvalue(), expected_output,
                         "適切なメッセージが表示されること")

    @patch('builtins.input', return_value='1')
    def test_choose_item(self, mock_input):
        items = [
            RecoveryAgents(),
            Bom()
        ]

        with redirect_stdout(StringIO()) as stdout:
            chosen_item = choose_item(items)

        self.assertEqual(chosen_item, items[0], "正しいアイテムが選択されること")
        self.assertIn(items[0].name, stdout.getvalue(), "選択されたアイテムが表示されること")

    @patch('builtins.input', return_value='0')
    def test_choose_item_cancel(self, mock_input):
        expected_output = "使用するアイテムを選んでください:\n1. 回復薬 - 体力を20回復するアイテム\n2. 爆弾 - 敵に50ダメージを与えるアイテム\n0. キャンセル\n"
        items = [
            RecoveryAgents(),
            Bom()
        ]

        with redirect_stdout(StringIO()) as stdout:
            chosen_item = choose_item(items)

        self.assertIsNone(chosen_item, "キャンセル時にNoneが返されること")
        self.assertEqual(stdout.getvalue(), expected_output, "正しい選択肢が表示されること")

    def test_reset_game(self):
        player = Player("勇者", 100, 20, 10)
        enemy_manager = EnemyManager()

        reset_game(player, enemy_manager)

        self.assertEqual(len(player.items), 3, "プレイヤーのアイテムが初期化されること")
        self.assertEqual(len(enemy_manager.enemies), 3, "敵のリストが初期化されること")

    def test_print_status(self):
        player = Player("勇者", 100, 20, 10)
        enemy = Enemy("ゴブリン", 30, 5, 8, 15)

        expected_output = "勇者: HP 100, MP 20\nゴブリン: HP 30\n"

        with redirect_stdout(StringIO()) as stdout:
            print_status(player, enemy)

        self.assertEqual(stdout.getvalue(), expected_output,
                         "正しいステータスが表示されること")


if __name__ == '__main__':
    unittest.main()
