def logger(func):
    def wrapper(*args, **kwargs):
        print("Функция запущена")
        result = func(*args, **kwargs)
        print("Функция завершена")
        return result
    return wrapper

def repeat(func):
    def wrapper(*args, **kwargs):
        for _ in range(3):
            func(*args, **kwargs)
    return wrapper

@logger
def greet():
    print("Привет!")

greet()

print("-" * 20)

@repeat
def greet_repeated():
    print("Привет!")

greet_repeated()