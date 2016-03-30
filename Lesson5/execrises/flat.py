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

import math

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


class Room:

    def __init__(self, width, length, height, window_width, door_width):
        self.width = width
        self.length = length
        self.height = height
        self.window_width = window_width
        self.door_width = door_width

    def __str__(self):
        return ('[Объект класса Room: width=%s, length=%s, height=%s, window_width=%s, door_width=%s]'
                % (self.width, self.length, self.height, self.window_width, self.door_width))

    def paintRoof(self, paint):
        roof_square = self.width * self.length
        return (roof_square / paint.square) * paint.price

    def putLaminate(self, laminate):
        floor_square = self.width * self.length
        return (floor_square / laminate.square) * laminate.price

    def glueWallpapers(self, wallpaper):
        walls_square = (self.width - self.door_width) * self.height + (self.length - self.window_width) * self.height
        return (walls_square / wallpaper.square) * wallpaper.price

    def fullPrice(self, paint, laminate, wallpaper):
        return self.paintRoof(paint) + self.putLaminate(laminate) + self.glueWallpapers(wallpaper)


class Flat:

    def __init__(self, rooms):
        self.rooms = rooms

    def __str__(self):
        return ('[Объект класса Flat: rooms=%s]'
                % (self.rooms))

    def addRoom(self, room):
        self.rooms.append(room)
        return self.rooms

    def removeRoom(self, room):
        self.rooms.remove(room)
        return self.rooms

    def countFullPrice(self, paint, laminate, wallpaper):
        self.fullprice = 0
        for room in self.rooms:
            self.fullprice += room.fullPrice(paint, laminate, wallpaper)
        return self.fullprice


a = Materials(12, 12)
b = Wallpaper(10, 0.6, 100)
c = Paint(5, 0.2, 50)
d = Laminate(0.2, 2, 10, 150)
e = Room(5, 3, 2.4, 1.4, 0.7)
f = Room(4, 4, 2.4, 1.4, 0.7)

print(a)
print(b)
print(c)
print(d)
print(e)
print(math.ceil(e.paintRoof(c)))
print(math.ceil(e.putLaminate(d)))
print(math.ceil(e.glueWallpapers(b)))
print(math.ceil(e.fullPrice(c, d, b)))

g = Flat([e, f])
print(g)
print(math.ceil(g.countFullPrice(c, d, b)))