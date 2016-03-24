#!/usr/bin/python3
__author__ = 'Отзовись, автор ;)' 

"""Упражнение "Количество слов"

Функция main() ниже уже определена и заполнена. Она вызывает функции 
print_words() и print_top(), которые вам нужно заполнить.

1. Если при вызове файла задан флаг --count, вызывается функция 
print_words(filename), которая подсчитывает, как часто каждое слово встречается 
в тексте и выводит:
слово1 количество1
слово2 количество2
...

Выводимый список отсортируйте в алфавитном порядке. Храните все слова 
в нижнем регистре, т.о. слова "Слон" и "слон" будут обрабатываться как одно 
слово.

2. Если задан флаг --topcount, вызывается функция print_top(filename),
которая аналогична функции print_words(), но выводит только топ-20 наиболее 
часто встречающихся слов, таким образом первым будет самое часто встречающееся 
слово, за ним следующее по частоте и т.д.

Используйте str.split() (без аргументов), чтобы разбить текст на слова.

Отсекайте знаки припинания при помощи str.strip() с знаками припинания 
в качестве аргумента.

Совет: не пишите всю программу сразу. Доведите ее до какого-то промежуточного 
состояния и выведите вашу текущую структуру данных. Когда все будет работать 
как надо, перейдите к следующему этапу.

Дополнительно: определите вспомогательную функцию, чтобы избежать дублирования 
кода внутри print_words() и print_top().

"""

import sys

# +++ваш код+++
# Определите и заполните функции print_words(filename) и print_top(filename).
# Вы также можете написать вспомогательную функцию, которая читает файл,
# строит по нему словарь слово/количество и возвращает этот словарь.
# Затем print_words() и print_top() смогут просто вызывать эту вспомогательную функцию.
def make_dict(filename):        # 2016.03.23_01:26:25 checked. prusanov
    file = open(filename, 'r', encoding='utf-8')
    words_list = file.read().split() #Получаем список слов
    striped_list = [word.lower().strip(".,!:;?()_+\"- ") for word in words_list] #Обрезаем знаки препинания для всех слов в списке
    set_words = set(striped_list) #Создаем множество (не будет повторения слов)
    words_dict = {elem: striped_list.count(elem) for elem in set_words} #Пробегаем по множеству слов и проверяем их количество в списке
    sorted_list = []       # аккуратней с такими именами
    for (key,value) in sorted(words_dict.items()):
        sorted_list.append((key,value))
    return sorted_list         # все же, лучше вернуть words_dict

def print_words(filename):      # 2016.03.23_01:29:20 checked. prusanov
    result = ''
    list = make_dict(filename)
    sorted_by_name = sorted(list, key=lambda elem: elem[0])
    for elem in sorted_by_name:
        result += elem[0] + " " + str(elem[1]) + "\n"       # лучше в цикле накапливать список, а не строку
    return print(result)        # print лучше оставлять отдельно, без return

def print_top(filename):        # 2016.03.23_01:30:41 checked. prusanov
    result = ''
    list = make_dict(filename)
    sorted_by_num = sorted(list, key=lambda elem: elem[1], reverse=True)
    for i in range(20):     # здесь можно проитерироваться по срезу  sorted_by_name[:20]
        result += sorted_by_num[i][0] + " " + str(sorted_by_num[i][1]) + "\n"
    return print(result)

###

# Это базовый код для разбора аргументов коммандной строки.
# Он вызывает print_words() и print_top(), которые необходимо определить.
def main():
    if len(sys.argv) != 3:
        print('usage: python wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
    main()
