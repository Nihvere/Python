import random
characters = 0
running = True
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*"
while running:
    print("\nРандомайзер поролей")
    characters = int(input("Символов в пороле (1-12) или 0 для завершения: "))
    
    if characters == 0:
        running = False
    elif characters < 8:
        print("Ошибка, слишком мало символов")
    elif characters > 12:
        print("Ошибка, слишком много символов")
    else:
        password = ""

        for _ in range(characters):
            password += random.choice(chars)
        print("Ваш надежный пороль:", password)