# параметры - начало и конец диапазона чисел
# сделал проверку на правильность параметров - если они не числа, скрипт ругается на юзера
from itertools import count
from sys import argv

_, my_start, my_end = argv
if my_start > my_end:
    my_end, my_start = my_start, my_end


def my_iterator(start: int, end: int) -> int:
    for el in count(start):
        if el > end:
            break
        else:
            yield el


try:
    my_print_var = list(my_iterator(int(my_start), int(my_end)))
except ValueError as e:
    my_print_var = 'Параметры должны быть целыми числами!'
finally:
    print(my_print_var)
