class Vehicle():
    def __init__(self, brand, speed):
        self.brand = brand
        self._speed = speed
        self._mileage = 0

    def get_info(self):
        print(f"Марка: {self.brand}")
        print(f"Скорость: {self._speed}")
        print(f"Пробег: {self._mileage}")

    def set_speed(self, value):
        if value < 0:
            self._speed = 0
        else:
            self._speed = value

    def move(self):
        self._mileage += 10
        print(f"{self.brand} едет со скоростью {self._speed} км/ч")

class Car(Vehicle):
    def __init__(self, brand, speed, doors):
        super().__init__(brand, speed)
        self.doors = doors

class Bicycle(Vehicle):
    def __init__(self, brand, speed, gear_count):
        super().__init__(brand, speed)
        self.gear_count = gear_count

    def move(self):
        self._mileage += 5
        print(f"{self.brand} едет на велосипеде со скоростью {self._speed} км/ч")


vehicle = Vehicle("Транспорт", 30)
car = Car("BMW", 120, 4)
bicycle = Bicycle("Stels", 25, 21)

vehicles = [vehicle, car, bicycle]

for v in vehicles:
    v.move()
