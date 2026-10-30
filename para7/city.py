class City:
    def __init__(self):
        self.__name_city = ""
        self.__name_region = ""
        self.__name_country = ""
        self.__count_people = 0
        self.__mail_index = 0
        self.__phone_code = 0
    def input_data(self):
        self.__name_city = (input("Название города: "))
        self.__name_region = (input("Название региона: "))
        self.__name_country = (input("Название страны: "))
        self.__count_people = int(input("Кол-во людей: "))
        self.__mail_index = int(input("Индекс почты: "))
        self.__phone_code = int(input("Код номера телефона: "))
    
    def show_data(self):
        print("-------------------------------------")
        print("Название города: ", self.__name_city)
        print("Название региона: ", self.__name_region)
        print("Название страны: ", self.__name_country)
        print("Кол-во людей: ", self.__count_people)
        print("Индекс почты: ", self.__mail_index)
        print("Код номера телефона: ", self.__phone_code)
    
    def get_city(self):
        return self.__name_city
    
    def get_region(self):
        return self.__name_region
    
    def get_country(self):
        return self.__name_country
    
    def get_people(self):
        return self.__count_people
    
    def get_mail(self):
        return self.__mail_index
    
    def get_phone(self):
        return self.__phone_code

city = City()

city.input_data()
city.show_data()

print("\n Название страны: ", city.get_country())