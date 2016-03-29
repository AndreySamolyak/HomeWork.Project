#!/usr/bin/python3

""" Ремонт в квартире 

Есть квартира (2 комнаты и кухня). В квартире планируется ремонт: нужно 
поклеить обои, покрасить потолки и положить пол.



Подсказка: для округления вверх и вниз используйте:
import math
math.ceil(4.2)  # 5
math.floor(4.2) # 4

Примечание: Для простоты, будем считать, что обои над окном и над дверью 
не наклеиваются.
----------------

Дополнительно:
Сделать у объекта квартиры метод, выводящий результат в виде сметы:

[Комната: ширина: 3 м, длина: 5 м, высота: 2.4 м]
Обои        400x6=2400 руб.
Краска     1000x1=1000 руб.
Ламинат     800x8=6400 руб.
[Комната: ширина: 3 м, длина: 4 м, высота: 2.4 м]
Обои        400x5=2000 руб.
Краска     1000x1=1000 руб.
Ламинат     800x7=5600 руб.
[Кухня: ширина: 3 м, длина: 3 м, высота: 2.4 м]
Обои        400x4=1600 руб.
Краска     1000x1=1000 руб.
Ламинат     800x5=4000 руб.
---------------------------
Итого: 25000 руб.

"""


class Materials:

    def __init__(self, square, price):
        self.square = square
        self.price = price

    def __str__(self):
        return ('[Объект класса Materials: square=%s, price=%s]'
                % (self.square, self.price))


class Wallpaper(Materials):

    def __init__(self, width, height, price):
        Materials.__init__(self, width * height, price)
        self.weight = width
        self.height = height

    def __str__(self):
        return ('[Объект класса Wallpaper: square=%s, price=%s, weight=%s, height=%s]'
                % (self.square, self.price, self.weight, self.height))


class Paint(Materials):

    def __init__(self, weight, consumption, price):
        Materials.__init__(self, weight / consumption, price)
        self.weight = weight
        self.consumption = consumption

    def __str__(self):
        return ('[Объект класса Paint: square=%s, price=%s, weight=%s, consumption=%s]'
                % (self.square, self.price, self.weight, self.consumption))


class Laminate(Materials):

    def __init__(self, width, height, quantity, price):
        Materials.__init__(self, width * height * quantity, price)
        self.width = width
        self.height = height
        self.quantity = quantity

    def __str__(self):
        return ('[Объект класса Laminate: square=%s, price=%s, width=%s, height=%s, quantity=%s]'
                % (self.square, self.price, self.width, self.height, self.quantity))

a = Materials(12, 12)
b = Wallpaper(10, 20, 100)
c = Paint(5, 0.2, 50)
d = Laminate(0.2, 2, 10, 150)

print(a)
print(b)
print(c)
print(d)