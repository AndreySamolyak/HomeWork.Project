import re

def extract_names(filename):
    """
    Получает имя файла.
    Возвращает данные из файла в виде словаря:
    {
    'София, Софья': ['3841 (6,0%)*', '3668 (6,2%)', '2127 (4,8%)',
        '826 (2,4%)', '193 (0,4%)',],
    'Виктория': ['2219', '1994', '1829', '1076', '1033'],
    ...
    }

    При написании регулярных выражений удобно держать перед глазами копию
    анализируемого текста. Вот как выглядит HTML-код в файле
    babynames_girls.html:

    <tr> <td width="66">
        1
    </td> <td width="151">
        София, Софья
    </td> <td width="85">
        3841 (6,0%)*
    </td> <td width="104">
        3668 (6,2%)
    </td> <td width="94">
        2127 (4,8%)
    </td> <td width="104">
        826 (2,4%)
    </td> <td width="104">
        193 (0,4%)
    </td> </tr>

    """
    # +++ваш код+++
    f = open(filename, encoding='utf-8')
    match = re.findall(r'(?:<td.*?>)(.*?)(?:</td>)', f.read(), re.S)
    striped_list = strings = list(map(lambda x: x.strip(), match))
    years_list = ['2012', '2010', '2005', '2000', '1990']
    babynames_dict = {}
    for i in range(1, len(striped_list), 7):
        babynames_dict[striped_list[i]] = {years_list[j]: (striped_list[i+j+1]).split() for j in range(5)}
    #print(babynames_dict)
    return babynames_dict


def print_names(babynames):
    # +++ваш код+++
    """
    1. Запрашивает у пользователя интересующий его год (желательно вывести список
        возможных вариантов и попросить ввести данные заново, если по указанному
        году нет данных).

    2. Выводит на печать данные в алфавитном порядке имен:
        Александра 1683
        Алина 837
        Алиса 1239
        Алёна, Алена 658
        Амина 243
        Анастасия 3055 (5,1%)
        ...
    """
    years = ['2012', '2010', '2005', '2000', '1990']
    checked_year = input("Выберите год рождения (2012, 2010, 2005, 2000, 1990) : ")
    sorted_list_by_year = []
    while checked_year not in years:
        checked_year = input("Для выбранного года статистика отсутсвует!\n"
                             "Выберите год рождения (2012, 2010, 2005, 2000, 1990) : ")
    for key, value in sorted(babynames.items()):
        #print(key + " " + value[years.index(checked_year)])
        sorted_list_by_year.append((key, value[checked_year]))
    sorted_list_by_year = sorted(sorted_list_by_year, key=lambda elem: int(elem[1][0]), reverse=True)
    for i in range(len(sorted_list_by_year)):
        if len(sorted_list_by_year[i][1]) == 2:
            print(sorted_list_by_year[i][0] + " " + sorted_list_by_year[i][1][0] + " " + sorted_list_by_year[i][1][1])
        else:
            print(sorted_list_by_year[i][0] + " " + sorted_list_by_year[i][1][0])
    return

filename = r'.\babynames\babynames_boys.html'
babynames = extract_names(filename)
print_names(babynames)