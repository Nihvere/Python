num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
operaton = input("Выберите операцию (1(+), 2(-), 3(:), 4(*): ")

def calculator(num1, num2, operation):
    if operation == "1":
        answer = num1 + num2
        return answer
    elif operation == "2":
        answer = num1 - num2
        return answer
    elif operation == "3":
        answer = num1 / num2
        if num2 == 0:
            return "Ошибка! Делить на ноль нельзя"
        return answer
    elif operation == "4":
        answer = num1 * num2
        return answer
    else:
        return "Неизвестная операция"

print(calculator(num1, num2, operaton))