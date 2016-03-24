'''
def make_dict(filename):
    file = open(filename, 'r', encoding='utf-8')
    words_list = file.read().split()
    words_dict = {elem.lower().strip(".,!:;?()_+\""): words_list.count(elem) for elem in words_list}
    return words_dict

def print_words(filename):
    dict = make_dict(filename)
    return

print(make_dict(".\\text.txt"))
print(print_words(".\\text.txt"))
'''

file = open(".\\test.txt", 'r', encoding='utf-8')
words_list = file.read().split()
striped_list = [word.lower().strip(".,!:;?()_+\"- ") for word in words_list]
set_words = set(striped_list)
words_dict = {elem: striped_list.count(elem) for elem in set_words}
print(words_list)
print(striped_list)
print(set_words)
print(words_dict)

'''
    print(words_dict)
print(sorted(words_dict.items()))
print("------------------------------------------------------------")
print(sorted(words_dict.values(), reverse=True))
'''
'''
result = ""
for (key,value) in sorted(words_dict.items()):
        result += key + " " + str(value) + "\n"
        #print(key + " " + str(value))
        #print(result)
print(result)
'''

'''
list = []
for (key,value) in sorted(words_dict.items()):
    list.append((key,value))
print(list)
print(sorted(list, key=lambda elem: elem[1], reverse=True))
'''

'''
import random
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
    str = ""
    for i in range(200):
        if word in mimic_dict.keys():
            add_word = random.choice(mimic_dict[word])
            result += add_word + " "
        else:
            add_word = random.choice(mimic_dict[str])
            result += add_word + " "
        word = add_word
    return print(result)

d = mimic_dict('text.txt')
print_mimic(d, '')
'''