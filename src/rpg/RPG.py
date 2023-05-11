# %%
import random


class Character:
    def __init__(self, name, health, mp, attack_damage):
        self.name = name
        self.health = health
        self.mp = mp
        self.attack_damage = attack_damage

    def attack(self, target):
        damage = random.randint(1, self.attack_damage)
        target.health -= damage
        print(f"{self.name}の攻撃！ {target.name}に{damage}のダメージ！")


class Player(Character):
    def __init__(self, name, health, mp, attack_damage):
        super().__init__(name, health, mp, attack_damage)
        self.level = 1
        self.exp = 0
        self.max_health = health
        self.max_mp = mp
        self.items = []

    def level_up(self):
        self.level += 1
        self.max_health += 10
        self.health = self.max_health
        print(f"{self.name}はレベル{self.level}にアップした！ HPが回復した！")

    def gain_exp(self, exp):
        self.exp += exp
        if self.exp >= pow(self.level, 2) * 10:
            self.level_up()
            self.exp = 0

    def use_item(self, item, target=None):
        if target is None:
            self.health = min(
                self.health + item.restore_amount, self.max_health)
            print(f"{self.name}は{item.name}を使って{item.restore_amount}のHPを回復した！")
        else:
            damage = item.attack_damage
            target.health -= damage
            print(f"{self.name}は{item.name}を使って{target.name}に{damage}のダメージを与えた！")
        self.items.remove(item)

    def add_item(self, item):
        self.items.append(item)


class Enemy(Character):
    def __init__(self, name, health, mp, attack_damage, exp_reward):
        super().__init__(name, health, mp,  attack_damage)
        self.exp_reward = exp_reward


class Goblin(Enemy):
    def __init__(self):
        super().__init__(
            name="ゴブリン",
            health=30,
            mp=5,
            attack_damage=8,
            exp_reward=15
        )


class Orc(Enemy):
    def __init__(self):
        super().__init__(
            name="オーク",
            health=40,
            mp=5,
            attack_damage=10,
            exp_reward=20
        )


class Slime(Enemy):
    def __init__(self):
        super().__init__(
            name="スライム",
            health=20,
            mp=0,
            attack_damage=5,
            exp_reward=10
        )


class HealingItem:
    def __init__(self, name, description, restore_amount):
        self.name = name
        self.description = description
        self.restore_amount = restore_amount
        self.kind = "回復"


class RecoveryAgents(HealingItem):
    def __init__(self):
        super().__init__(
            name="回復薬",
            description="体力を20回復するアイテム",
            restore_amount=20
        )


class AttackItem:
    def __init__(self, name, description, attack_damage):
        self.name = name
        self.description = description
        self.attack_damage = attack_damage
        self.kind = "攻撃"


class Bom(AttackItem):
    def __init__(self):
        super().__init__(
            name="爆弾",
            description="敵に50ダメージを与えるアイテム",
            attack_damage=50
        )


class EnemyManager:
    def __init__(self):
        self.enemies = []
        self.current_enemy = None

    def add_enemy(self, enemy):
        self.enemies.append(enemy)

    def next_enemy(self):
        if not self.enemies:
            return  # 敵がいない場合は何もしない

        self.current_enemy = self.enemies.pop(0)

        print(f"{self.current_enemy.name}が現れた！")

    def reset(self):
        self.enemies = [Goblin(), Orc(), Slime()]  # 敵のリストを最初から初期化する
        self.current_enemy = None

    def is_defeated(self):
        return not self.enemies  # 敵が全滅した場合はTrueを返す


def get_valid_input(choices):
    while True:
        choice = input("選択肢を入力してください: ")
        if choice in choices:
            return choice
        else:
            print("無効な選択です。再度入力してください。")


def choose_item(items):
    print("使用するアイテムを選んでください:")
    for i, item in enumerate(items):
        print(f"{i+1}. {item.name} - {item.description}")

    print("0. キャンセル")
    valid_choices = [str(i) for i in range(len(items)+1)]
    choice = get_valid_input(valid_choices)

    if choice == "0":
        return None

    return items[int(choice)-1]


def reset_game(player, enemy_manager):
    player.add_item(RecoveryAgents())
    player.add_item(RecoveryAgents())
    player.add_item(Bom())
    enemy_manager.reset()


def print_status(player, enemy):
    print(f"{player.name}: HP {player.health}, MP {player.mp}")
    print(f"{enemy.name}: HP {enemy.health}")


def main():
    player = Player("勇者", 100, 20, 10)
    player.add_item(RecoveryAgents())
    player.add_item(RecoveryAgents())
    player.add_item(Bom())
    enemy_manager = EnemyManager()
    enemy_manager.add_enemy(Goblin())
    enemy_manager.add_enemy(Orc())
    enemy_manager.add_enemy(Slime())

    print("冒険を開始します！")

    while True:
        enemy_manager.next_enemy()
        enemy = enemy_manager.current_enemy

        while True:
            print_status(player, enemy)

            choice = input("1. 攻撃する 2. アイテムを使う 3. 逃げる\n")

            if choice == "1":
                player.attack(enemy)

            elif choice == "2":
                item = choose_item(player.items)
                if not item:
                    continue

                if item.kind == "回復":
                    if player.health == player.max_health:
                        print("体力は既に満タンです！")
                        continue

                    player.use_item(item)

                elif item.kind == "攻撃":
                    player.use_item(item, enemy)

            elif choice == "3":
                if random.random() > 0.5:  # 50%の確率で失敗する。
                    print("逃げ出しました！")
                    enemy_manager.next_enemy()
                    continue
                else:
                    print("捕まりました！")

            if enemy.health <= 0:
                print(f"{enemy.name}を倒した！")
                player.gain_exp(enemy.exp_reward)
                if enemy_manager.is_defeated():
                    break  # ゲームクリアの条件を満たした場合はゲームを終了する

                enemy_manager.next_enemy()
                enemy = enemy_manager.current_enemy
                continue
                # 次の敵が現れた場合は次のターンに移行する

            enemy.attack(player)
            if player.health <= 0:
                print(f"{player.name}は敗北しました！")
                break

        if player.health > 0:
            print("ゲームクリア！")
        else:
            print("ゲームオーバー！")

        retry = input("1. もう一回やる 2. 終了する\n")
        if retry == "1":
            reset_game(player, enemy_manager)
        else:
            print("(^U^)")
            break


if __name__ == "__main__":
    main()


# %%
