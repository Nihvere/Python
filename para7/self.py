class Human:
    def __init__(self):
        self.__full_name = ""
        self.__birth_day = ""
        self.__phone = ""
        self.__city = ""
        self.__country = ""
        self.__adress = ""

    def input_data(self):
        self.__full_name = (input("Введите ФИО: "))
        self.__birth_day = (input("Введите день рождение: "))
        self.__phone = (input("Введите номер телефона: "))
        self.__city = (input("Введите город: "))
        self.__country = (input("Введите страну: "))
        self.__adress = (input("Введите адрес: "))
    
    def show_data(self):
        print("-------------------------------------")
        print("ФИО: ", self.__full_name)
        print("День рождения: ", self.__birth_day)
        print("Номер телефона: ", self.__phone)
        print("Город: ", self.__city)
        print("Страна: ", self.__country)
        print("Адрес: ", self.__adress)

person = Human()

person.input_data()
person.show_data()