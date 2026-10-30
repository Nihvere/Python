# Создаем класс фрукта
class Fruct:
    pass
# a и b ссылаются на класс Fruct
a = Fruct()
b = Fruct()
# Делаем атрибут a = Fruct, банан с весом в 200 грамм
a.name = 'banana'
a.weight = 200
# Делаем атрибут b = Fruct, яблоко с весом 140 грамм
b.name = 'apple'
b.weight = 140
# Обращаемся к a, b к их именни и к атрибуту веса и выводим
print(a.name, a.weight, "\n",b.name, b.weight)
