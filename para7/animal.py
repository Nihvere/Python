# class Animal:
#     def __init__(self, name, health):
#         self.name = name
#         self.health = health
        
#     def show_info(self):
#         print("Name: ", self.name)
#         print("Health: ", self.health)
    
#     def eat(self):
#         self.health += 10
#         print(self.name, "поел и восстановил здоровье")

# animal = Animal("Worav", 100)
# animal.show_info()
# animal.eat()
# animal.show_info()

# class Cat(Animal):
#     def meow(self):
#         print(f"{self.name} say Meow!")

# class Dog(Animal):
#     def bark(self):
#         print(f"{self.name} say Gaf Gaf!")

# cat = Cat("Fentonil", 100)
# dog = Dog("Smasher", 60)
# print("="*30)
# cat.show_info()
# cat.eat()
# cat.meow()
# print("="*30)
# dog.show_info()
# dog.eat()
# dog.bark()

class Animal:
    def __init__(self, name, health):
        self.name = name
        self.health = health

class Dog(Animal):
    def __init__(self, name, health, breed):
        super().__init__(name, health)
        self.breed = breed

    def show_info(self):
        print("Name: ", self.name)
        print("Health: ", self.health)
        print("Breed: ", self.breed)
dog = Dog("Mentol", 120, "Germany shepherd")
dog.show_info()