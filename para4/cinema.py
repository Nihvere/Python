seats = ["0"] * 10
price = 2500
tickets = 0
total = 0
running = True
while running:
    print("\nСхема зала:")
    for i in range(10):
        print("[" + seats[i] + "]", end=" ")

    place = int(input("\nВведите место (1-10) или 0 для завершения: "))
    
    if place == 0:
        running = False
    elif place < 1 or place > 10:
        print("Ошибка! Такого места нет.")
    elif seats[place - 1] == "X":
        print("Ошибка! Место уже занято.")
    else:
        seats[place - 1] = "X"
        tickets += 1
        total += price
        print("Место", place, "успешно забронировано!")

print("\n----- ЧЕК -----")
print("Куплено билетов:", tickets)
print("К оплате:", total, "тенге")