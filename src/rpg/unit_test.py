import unittest
from test.support import captured_stdout


from RPG import Character, Player, HealingItem, AttackItem, RecoveryAgents, Bom, EnemyManager, Enemy, Goblin, Orc, Slime, choose_item, reset_game, print_status, main


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


class HealingItemEnemyTestCase(unittest.TestCase):
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


class AttackItemEnemyTestCase(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()
