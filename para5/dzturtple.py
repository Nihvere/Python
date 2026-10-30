import turtle

number = [100, 150, 90]
def num(number):
    turtle.forward(number[1])
    turtle.left(number[2])
    turtle.forward(number[0])
    turtle.left(number[2])
    turtle.forward(number[1])
    turtle.left(number[2])
    turtle.forward(number[0])

def pol():
    turtle.circle(100, 180)

turtle.done()