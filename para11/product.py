def product(func):
    def wrapper(in_stock):
        if in_stock:
            func(in_stock)
        else:
            print("Товара нет в наличии.")
    return wrapper

@product
def buy(in_stock):
    print("Успешно оформлен заказ")

buy(True)
buy(False)