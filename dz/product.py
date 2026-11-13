class Product():
    def __init__(self, name, price, quantity):
        if price <0 or quantity <0:
            raise ValueError("Цена и количество не могут быть отрицательными!")
        self.name = name
        self.price = price
        self.quantity = quantity

    def show_info(self):
        print(f"Название: {self.name}, Стоимость: {self.price} тенге, Количество: {self.quantity}")

class Cart():
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f'{product.name} добавлен в корзину!')

    def remove_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                print(f"{name} удалён из корзины!")
                return
        print(f"Товар {name} не найден в корзине!")

    def get_total(self):
        total = 0
        for product in self.products:
            total += product.price * product.quantity

        return total


    def show_cart(self):
        if not self.products:
            print("Корзина пуста!")
            return
        
        print("\n--- Ваша корзина ---")

        for product in self.products:
            product.show_info()
            print("-------------------")

        print(f"Итоговая стоимость: {self.get_total()} тенге.")

product1 = Product("Ноутбук", 50000, 2)
product2 = Product("Мышка", 1500, 3)
product3 = Product("Клавиатура", 3000, 1)

cart = Cart()

cart.add_product(product1)
cart.add_product(product2)
cart.add_product(product3)

cart.show_cart()

cart.remove_product("Мышка")

cart.show_cart()
