class Student():
    def __init__(self, name, points):
        self._name = name
        self._points = int(points)

    def add_points(self, amount):
        if amount > 0:
            self._points += amount
        else:
            print("Ошибка!")

    def show_points(self):
        print(f'Name: {self._name} | Points: {self._points}')
        return self._points

class OnlineStudent(Student):
    def __init__(self, name, points, course):
        super().__init__(name, points)
        self._course = course
    
    def study(self):
        print(f'Курс: {self._course}')

class PythonStudent():
    def learn(learn):
        print("Изучаю Python")

class JavaStudent():
    def learn(learn):
        print("Изучаю Java")

student = PythonStudent()

def start_learning(student):
    student.learn()

# start_learning(student)

# student1 = OnlineStudent("Andrey", 1300, "Курс")
# student1.show_points()
# student1.add_points(500)
# student1.show_points()
# student1.study()