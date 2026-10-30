# Простой калькулятор на Python
num1=int(input("Введите первое число: "))
operation=input("Введите операцию (+, -, *, /): ")
num2=int(input("Введите второе число: "))
# Проводим операцию в зависимости от введенной операции
if operation=='+':
    print(str(num1),"+",str(num2),"=",num1+num2)
elif operation=='-':
    print(str(num1),"-",str(num2),"=",num1-num2)
elif operation=='*':
    print(str(num1),"*",str(num2),"=",num1*num2)
elif operation=='/':
    if num2==0:
        print("Ошибка: деление на ноль!")
    else:
        print(str(num1),"/",str(num2),"=",num1/num2)