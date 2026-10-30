class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.happiness = 0
        self.life = True
        self.happy = ""

    def clamp_stats(self):
        self.hunger = max(0, min(100, self.hunger))
        self.happiness = max(0, min(100, self.happiness))

    def rules(self):
        self.clamp_stats()
        

        if self.hunger >= 100:
            self.life = False
        
        if self.life == False:
            print(f'{self.name} Умер!')
    
    def feed(self):
        self.hunger -= 20
        self.clamp_stats()
    def play(self):
        self.happiness += 10
        self.clamp_stats()
    
    def status(self):
        print("--- Статистика ---")
        print(f'Имя: {self.name}')
        print(f'Голод: {self.hunger}')
        print(f'Счастье: {self.happiness}, {self.happ}')
    
    def update_happ(self):
        if self.happiness >= 80:
            self.happ = "😊 Питомец счастлив!"
        elif self.happiness >= 40:
            self.happ = "😐 Питомец доволен."
        elif self.happiness <= 40:
            self.happ = "😢 Питомцу грустно."
    
    def function(self):
        self.rules()

        if not self.life:
            return

        print(
            f"1. Статистика / "
            f"2. Покормить {self.name} / "
            f"3. Поиграть с {self.name}"
        )

        func = input("Выберите функцию (1/2/3): ")

print("Выбери имя своему питомцу: ")
name = input()
peto = Pet(name)
peto.function()