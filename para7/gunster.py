import random
class Gunster:
    def __init__(self):
        self.name = ""
        self.health = 0
        self.damage = 0
        self.life = True

    def input_data(self):
        self.name = input("Введите имя: ")
        self.health = int(input("Введите кол-во здоровья: "))

    def take_damage(self, amount):
        self.health -= amount
        
        if self.health <= 0:
            self.health = 0
            self.life = False
            print("Death")

        print("--- Происходит атака ---")
        print(f'{self.name} получил {amount} Урона')
        print(f'осталось здоровья: {self.health}')
    
    def attack(self, enemy):
        if self.health and enemy.life:
            enemy.take_damage(random.randint(1, 100))

gunster_one = Gunster()
gunster_two = Gunster()
print("--- Первый ---")
gunster_one.input_data()
print("--- Второй ---")
gunster_two.input_data()
print("--------------- Дуэль начинается ---------------")

while gunster_one.life and gunster_two.life:
    gunster_one.attack(gunster_two)
    if not gunster_two.life:
        break
    
    gunster_two.attack(gunster_one)

print("--------------- Дуэль окончена ---------------")
if gunster_one.life:
    print(f'Победил {gunster_one.name}!')
else:
    print(f'Победил {gunster_two.name}!')