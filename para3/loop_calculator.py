while True:
    num1=int(input("Введите число (n-выход): "))
    operation=input("Введите операцию (+, -, *, /): ")
    num2=int(input("Введите число: "))

    if num1=='n':
        break
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