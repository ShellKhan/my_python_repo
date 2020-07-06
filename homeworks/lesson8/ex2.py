# encoding: utf-8
class MyZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt


while True:
    teststr = input('Введите два числа через пробел: ').split(' ')
    if len(teststr) == 2:
        try:
            divided = int(teststr[0])
        except ValueError:
            print('Ошибка ввода! Делимое - не число.')
            continue
        try:
            divider = int(teststr[1])
        except ValueError:
            print('Ошибка ввода! Делитель - не число.')
            continue
        try:
            if not divider:
                raise MyZeroDivisionError('Делить на ноль нельзя!')
            else:
                print(f'{divided} / {divider} = {divided / divider}')
                break
        except MyZeroDivisionError as info:
            print(info)
            continue
    print('Ошибка ввода! Чисел должно быть два.')
