def bio(name, *args, **kwargs):
    print("Имя:", name)
    print("Факты:", args)
    print("Инфо:", kwargs)


bio("Сергей", "Программист", "Любит кофе", возраст=15, город="Атырау")
