def logger(func):
    def wrapper(*args, **kwargs):
        print("Функция запущена")
        print(f"Переданные аргументы: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print("Функция завершена")
        return result
    return wrapper

@logger
def user_info(name, age, city):
    info = f"Имя: {name}, Возраст: {age}, Город: {city}"
    print(info)
    return info

result = user_info("Али", 20, city="Атырау")