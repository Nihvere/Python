import random

player1 = 0
player2 = 0
finish = 50

def cube(num_dice):
    number = random.randint(1, 6)
    return number

while True:
    solution = input("Подбросить кубик? 1(Да) | 2(Нет): ")

    if solution == "1":
        roll = cube(0)
        player1 = player1 + roll

        print("Выпало:", roll)
        print("Всего очков у вас:", player1)
        print("-" * 30)

        if player1 >= finish:
            print("Поздравляю, вы победили!")
            break

    elif solution == "2":
        print("Игра окончена.")
        break

    else:
        print("Введите 1 или 2!")
        continue

    input("Нажмите Enter... для хода второго игрока")

    roll2 = cube(0)
    player2 = player2 + roll2

    print("Врагу выпало:", roll2)
    print("Всего очков у врага:", player2)

    if player2 >= finish:
        print("Победил второй игрок!")
        break