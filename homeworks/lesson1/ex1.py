# Здесь и далее мне не удалось найти простую функцию, позволяющую опознавать введенные отрицательные числа:
# строки вида "-10" опознаются как не числа.
# Поэтому отрицательные числа вводить не надо.

var_int_1 = 0
var_int_2 = 100
var_int_input = input('Введите число: ')
if (not var_int_input.isdigit()):
    print('А это не число...')
else:
    var_int_input = int(var_int_input)
    if (var_int_input & 1) == 0:
        print('Это число четное!')
    else:
        print('Это число нечетное!')
var_str_1 = 'это строка'
var_str_2 = "это тоже строка"
var_str_input = input('Введите строку: ')
print(var_str_1 + ' и ' + var_str_2)
print(var_str_input * 3)