import sys

def extract_names(filename):
    f = open(filename, encoding='utf-8')
    lines = f.read()
    return lines


def main():
    # Код разбора командной строки
    # Получим список аргументов командной строки, отбросив [0] элемент,
    # который содержит имя скрипта
    args = sys.argv[1:]

    if not args:
        print('usage: filename')
        sys.exit(1)

    filename = args[0]
    babynames = extract_names(filename)
    print(babynames)


if __name__ == '__main__':
    main()