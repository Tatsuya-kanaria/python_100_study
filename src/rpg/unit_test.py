import unittest
from test.support import captured_stdout


from RPG import Character, Player, RecoveryAgents, Bom, EnemyManager, Enemy, Goblin, Orc, Slime, choose_item, reset_game, print_status, main


class CharacterTestCase(unittest.TestCase):
    def setUp(self):
        # テストの前準備を行う
        self.character = Character("勇者", 100, 20, 10)

    def tearDown(self):
        # テストの後始末を行う
        self.character = None

    def test_character_name(self):
        self.assertEqual(self.character.name, "勇者")

    def test_character_health(self):
        self.assertEqual(self.character.health, 100)

    def test_character_mp(self):
        self.assertEqual(self.character.mp, 20)

    def test_character_attack_damage(self):
        self.assertEqual(self.character.attack_damage, 10)

    def test_character_attack(self):
        target = Character("敵", 50, 10, 10)

        with captured_stdout() as stdout:
            self.character.attack(target)
            result = [
                50 - damage for damage in range(1, self.character.attack_damage + 1)]
            self.assertIn(target.health, result)

            expected_output = f'勇者の攻撃！ 敵に{50 - target.health}のダメージ！\n'
            self.assertEqual(stdout.getvalue(), expected_output)


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

    def test_player_initial_level(self):
        self.assertEqual(self.player.level, 1)

    def test_player_initial_exp(self):
        self.assertEqual(self.player.exp, 0)

    def test_max_health(self):
        self.assertEqual(self.player.max_health, 100)

    def test_max_mp(self):
        self.assertEqual(self.player.max_mp, 20)

    def test_initial_items_is_none(self):
        self.assertEqual(self.player.items, list())

    def test_level_up(self):
        expected_level = self.player.level + 1
        expected_max_health = self.player.max_health + 10
        expected_output = f'{self.player.name}はレベル{expected_level}にアップした！ HPが回復した！\n'

        with captured_stdout() as stdout:
            self.player.level_up()

            self.assertEqual(self.player.level, expected_level)
            self.assertEqual(self.player.max_health, expected_max_health)
            self.assertEqual(stdout.getvalue(), expected_output)

    def test_gain_exp(self):
        self.player.gain_exp(1)

        self.assertEqual(self.player.exp, 1)

        # 標準出力を表示させないため
        with captured_stdout() as stdout:
            self.player.gain_exp(self.exp)

            self.assertEqual(self.player.exp, 0)

    def test_use_recovery_item(self):
        self.player.add_item(self.recovery_item)
        # ダメージを想定
        self.player.health -= 50

        except_health = min(
            self.player.max_health, self.player.health + self.recovery_item.restore_amount)
        except_output = f"{self.player.name}は{self.recovery_item.name}を使って{self.recovery_item.restore_amount}のHPを回復した！\n"

        with captured_stdout() as stdout:
            self.player.use_item(self.recovery_item, target=None)

            self.assertEqual(self.player.health, except_health)
            self.assertEqual(stdout.getvalue(), except_output)
            self.assertNotIn(self.recovery_item, self.player.items)

    def test_use_attack_item(self):
        self.player.add_item(self.attack_item)

        except_enemy_health = self.enemy.health - self.attack_item.attack_damage
        except_output = f"{self.player.name}は{self.attack_item.name}を使って{self.enemy.name}に{self.attack_item.attack_damage}のダメージを与えた！\n"

        with captured_stdout() as stdout:
            self.player.use_item(self.attack_item, target=self.enemy)

            self.assertEqual(self.enemy.health, except_enemy_health)
            self.assertEqual(stdout.getvalue(), except_output)
            self.assertNotIn(self.attack_item, self.player.items)

    def test_add_item(self):
        self.player.add_item(self.recovery_item)

        self.assertIn(self.recovery_item, self.player.items)
        self.assertNotIn(self.attack_item, self.player.items)


class EnemyTestCase(unittest.TestCase):
    def setUp(self):
        # test の前準備をする
        self.player = Player("勇者", 100, 20, 10)
        self.enemy = Enemy(
            name="ゴブリン",
            health=30,
            mp=5,
            attack_damage=8,
            exp_reward=15)

    def tearDown(self):
        # テストの後始末を行う
        self.player = None

    def test_enemy_exp_rewards(self):
        self.assertEqual(self.enemy.exp_reward, 15)


if __name__ == '__main__':
    unittest.main()
