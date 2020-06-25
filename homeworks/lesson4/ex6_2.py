# в качестве списка я использовал строку, так как она все равно что список букв
# параметр при запуске - число выводимых букв
# обработку неправильного параметра не делал: если не число - пусть валится.
from itertools import cycle
from sys import argv

_, my_stop = argv
my_line = 'qwertyuiop'
my_stop = int(my_stop)


def my_iterator(source: str, stop: int) -> int:
    counter = 1
    for el in cycle(source):
        if counter <= stop:
            yield el
            counter += 1
        else:
            break


my_print_var = list(my_iterator(my_line, my_stop))
print(my_print_var)
