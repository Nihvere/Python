
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print("Имя:", self.name)
        print("Возраст:", self.age)


class Lion(Animal):
    def roar(self):
        print("Р-р-р!")


class Monkey(Animal):
    def jump(self):
        print("Обезьяна прыгает по деревьям!")


class Elephant(Animal):
    def spray_water(self):
        print("Слон обливает себя водой!")


lion = Lion("Симба", 5)
monkey = Monkey("Чита", 3)
elephant = Elephant("Дамбо", 8)

lion.show_info()
lion.roar()

monkey.show_info()
monkey.jump()

elephant.show_info()
elephant.spray_water()
