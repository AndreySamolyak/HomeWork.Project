# Интерактивный цикл ввода данных
run = True
while run:
    a = input('Введите число или stop: ')
    if a == 'stop':
        run = False
    else:
        try:
            a = float(a)
        except:
            print('error')
        else:
            print(a**2)
else:
    print('Bye!')