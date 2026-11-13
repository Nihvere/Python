import time
def delivery_timer(func):
    def wrapper(*args, **kwargs):
        print("Принимаем новый заказ...")
        time.sleep(3)
        func(*args, **kwargs)

        if kwargs.get("express") is True:
            print("Доставка займет 20 минут!")
        else:
            print("Доставка займет 60 минут!")
    return wrapper

@delivery_timer
def order_pizza(*toppings, **details):
    price = 2000 + len(toppings)*300
    print(f"Состав заказа: \n - Добавки: {toppings} \n - Детали заказа: {details} \n Общая стоимость: {price}")

order_pizza("сыр", "грибы", size="средняя")
print("-" * 30)
order_pizza("пепперони", "халапеньо", "оливки", express=True, address="ул. Абая 10")