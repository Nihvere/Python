like_items = {"Магнит", "Фотоаппарат", "Будильник"}
attempts = 3
running = True
print("Угадай одну из моих любимых вещей!")
print("У вас есть", attempts , "попытки.")
while attempts >= 0 and running:
    print(f"\nОсталось попыток: {attempts}")
    guess_item = input("Введите вариант: ")
    if guess_item in like_items:
        print("Поздравляю вы угадали предмет: ", guess_item)
        running = False
    else:
        attempts -= 1
        if attempts > 0:
            print("Вы не угадали у вас осталось: ", attempts, "Попыток!")
        else:
            print("Вы проиграли!")