def door(func):
    def open_door():
        print("Открыл дверь")
        func()
        print("Закрыл дверь")
    
    return open_door

@door
def log_in():
    print("Вошел в комнату")

log_in()

# def wrapper(func):
#     def student(name, age, passed):
#         print("-"*30)
#         print(f'Имя студента {name}')
#         print(f'Возраст студента {age}')
#         func(name, age, passed)
#     return student
# @wrapper
# def is_passed(name, age, passed):
#     print(f'Имя: {name}. Возраст: {age}. Прошел: {passed}')

# is_passed("Олег", 17, True)
# is_passed("Абдурахмангаджи", 16, False)