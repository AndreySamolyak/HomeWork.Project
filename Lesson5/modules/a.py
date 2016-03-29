# Любой файл может импортировать функциональные возможности из любого 
# другого файла. 
import Lesson5.modules.b
Lesson5.modules.b.spam('Hello')

# можно импортировать только нужные вам имена
from Lesson5.modules.b import foo, bar

print(foo, bar)
foo = 4

# можно импортировать все имена модуля в область видимости
from Lesson5.modules.b import *
spam('Hey Hey Hey')

# двойное импортирование
# a может использовать имена из b и с. однако обратное не верно:
# c не имеет доступа к b, а b к а.
Lesson5.modules.b.c.printing('c?')


# доступ к именам модуля
print(Lesson5.modules.b.__dict__.keys())
print(dir(Lesson5.modules.b))


# from string import ascii_letters # ImportError: cannot import name ascii_letters
# при наличии файла string.py в папке с проектом он будет воспринят как
# модуль, и при импорте будет импортирован именно он


import sys
import pprint
pprint.pprint(sys.path)

# Поиск модуля ведется с начала списка, и не случайно первой стоит текущая 
# папка. Модуль из текущей папки загрузится первым, перекрыв остальные.
# Поэтому не пытайтесь создавать свои модули с именами pickle или urllib - 
# они перекроют стандартные и вы получите странную ошибку при импорте.

# Полное имя модуля. Путь от начала с точками как разделителями.
print(__name__)


