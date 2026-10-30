inventory = {"меч", "щит", "зелье"}
print("В инвенторе: ", inventory, end="\n\n")
inventory.add("лук")
print("В инвенторе: ", inventory, end="\n\n")
inventory.remove("щит")
print("В инвенторе: ", inventory, end="\n\n")
print("В инвенторе есть ли меч? ", ("меч") in inventory, end="\n\n")
print("Количество предметов: ", len(inventory), "\nПредметы: ", inventory)