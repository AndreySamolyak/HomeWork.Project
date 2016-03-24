'''
# В начале импортируются модули - sys один из стандартных
import sys
# Основной код скрипта в функции main()
def main():
    print('Hello there', sys.argv)
# Аргументы командной строки: sys.argv[1], sys.argv[2] ...
# sys.argv[0] содержит само название скрипта
# Стандартный шаблон вызова функции main(),
# чтобы начать программу
if __name__ =='__main__':
    main()
'''

'''
# Определим функцию «repeat», принимающую 2 аргумента
def repeat(s, exclaim):
    """Возвращает строку s, повторенную 3 раза.
    Если exclaim == True — поставим восклицательные знаки.
    """
    result = s + s + s  # также можно использовать "s * 3"
    if exclaim:
        result = result + '!!!'
    return result

print(repeat('hello', True))
'''

'''
template = '{0}, {1} and {2}'  # Порядковые номера позиционных
print(template.format('spam', 'ham', 'eggs'))

template = '{motto}, {pork} and {food}' # Имена именованных
print(template.format(motto='spam', pork='ham', food='eggs'))

template = '{motto}, {0} and {food}' # Оба варианта
print(template.format('ham', motto='spam', food='eggs'))
'''

'''
squares = [1, 4, 9, 16]
sum = 0
for num in squares:
    sum += num
print(sum) ## 30
'''

'''
list = ['larry', 'curly', 'moe']
if 'curly' in list:
    print('yay')
'''

'''
## print the numbers from 0 through 99
for i in range(10):
    print(i)
'''

'''
# Выведем каждый 3й элемент списка
a = ['larry', 'curly', 'moe']
i = 0
while i < len(a):
    print(a[i])
    i = i + 1
'''

'''
a = [5, 1, 4, 3]
print(sorted(a))
print(a)
'''

'''
strs = ['aa', 'BB', 'zz', 'CC']
print(sorted(strs))
print(sorted(strs, reverse=True))
'''

'''
strs = ['ccc', 'aaaa', 'd', 'bb']
print(sorted(strs, key=len))
'''

'''
import sys
help(len)
help(list.append)
dir(sys)
'''

'''
def inside(s):      # 2016.03.17_10:42:18 checked. prusanov
    # +++ ваш код +++
                        # PEP-8 не рекомендует использовать длинные строки
                        # подумайте, как можно обойтись без преобразования в int
                        # len() / 2 удобно было бы вынести в отдельную переменную
    halflen = len(s.split())//2
    return " ".join(s.split()[1:halflen:1] + s.split(" ")[::len(s.split())-1] + s.split(" ")[halflen:-1:1])


print(inside('a b c d e f'))
'''


