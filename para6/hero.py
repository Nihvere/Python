hero_team = {}
for i in range(3):
    print("\nГерой №,", i + 1, ":")
    name = input("Введите имя героя: ")

    item1 = input("Введите 1-ю вещь: ")
    item2 = input("Введите 2-ю вещь: ")
    item3 = input("Введите 3-ю вещь: ")
    
    items = [item1, item2, item3]

    hero_team[name] = items

for hero, items in hero_team.items():
    print("-" * 30)
    print("Герой: ", hero)
    print("Вещи с собой:", items)