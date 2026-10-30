# Импортируем turtle даем скинчик синий черепашке
import turtle
turtle.shape("turtle")
turtle.color("blue")
# треугольник
def triangle():
    count = 0
    while count <= 2:
        count = count +1
        turtle.forward(100)
        turtle.left(120)
# круг
def circle():
    # settings = int(input("Введите диаметр круга: "))
    # turtle.circle(settings)
    turtle.circle(80)
#звезда
def star():
    count = 0
    while count <= 4:
        count = count + 1
        turtle.forward(130)
        turtle.right(144)
# квадрат
def square():
    count = 0
    while count <=3:
        count = count +1
        turtle.forward(80)
        turtle.left(90)

triangle()
turtle.forward(150)
circle()
turtle.forward(60)
star()
turtle.forward(150)
square()

turtle.done()