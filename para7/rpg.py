class Character:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
        self.level = 1
        self.exp = 0

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
        print(f'{self.name} получил {amount} Урона')
        print(f'осталось здоровья: {self.health}')

    def attack(self, enemy):
        enemy.take_damage(self.damage)

hero = Character("Маг", 100, 25)
enemy = Character("Огр", 150, 20)
goblin = Character("Гоблин", 80, 10)

print(goblin.health)
goblin.attack(goblin)
print(goblin.health)

# print("--- Статы врага ---")
# print(enemy.name)
# print(enemy.health)
# print(enemy.damage)

# print("--- Статы героя ---")
# print(hero.name)
# print(hero.health)
# print(hero.damage)