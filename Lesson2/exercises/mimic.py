#!/usr/bin/python3

"""Имитация текста

Прочитайте файл, указанный в командной строке.
Используйте str.split() (без аргументов) для получения всех слов в файле.
Вместо того, чтобы читать файл построчно, проще считать
его в одну гигантскую строку и применить к нему split() один раз.

Создайте "имитационный" словарь, который связывает каждое слово
со списком всех слов, которые непосредственно следуют за этим словом в файле.
Список слов может быть в любом порядке и должен включать дубликаты. 

Так, например, для текста "Привет, мир! Привет, Вселенная!" мы получим такой
имитационный словарь:
{'': ['Привет,'], 'Привет,': ['мир!', 'Вселенная!'], 'мир!': ['Привет,']}
Будем считать, в качестве ключа для первого слова в файле используется пустая строка.

С помощью имитационного словаря довольно просто генерировать случайные тексты, 
имитирующие оригинальный. Возьмите слово, посмотрите какие слова могут за ним, 
выберите одно из них наугад, выведите его и используйте это слово 
в следующей итерации.

Используйте пустую строку в качестве ключа для первого слова.
Если вы когда-нибудь застрянете на слове, которого нет в словаре,
вернетесь к пустой строке, чтобы продолжать генерацию текста.

Примечание: стандартный python-модуль random включает в себя метод 
random.choice(list), который выбирает случайный элемент из непустого списка.

"""

import random
import sys


def mimic_dict(filename):
    """Возвращает имитационный словарь, сопоставляющий каждое слово
    со списом слов, которые непосредственно следуют за ним в тексте"""
    # +++ваш код+++
    file = open(filename, 'r', encoding='utf-8')
    words_list = file.read().split()
    dict = {}
    str = ''
    for word in words_list:
        if not str in dict:
            dict[str] = [word]
        else:
            if word not in dict[str]:
                dict[str].append(word)
        str = word
    return dict


def print_mimic(mimic_dict, word):
    """Принимает в качестве аргументов имитационный словарь и начальное слово,
    выводит 200 случайных слов."""
    # +++ваш код+++
    result = ""
    for i in range(200):
        if word in mimic_dict.keys():
            add_word = random.choice(mimic_dict[word])
            result += add_word + " "
        else:
            add_word = random.choice(mimic_dict[""])
            result += add_word + " "
        word = add_word
    return print(result)


def main():
    if len(sys.argv) != 2:
        print('usage: ./mimic.py file-to-read')
        sys.exit(1)

    d = mimic_dict(sys.argv[1])
    print_mimic(d, '')


if __name__ == '__main__':
    main()
