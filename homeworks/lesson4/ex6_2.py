# не понял насчет списка, определенного заранее. если можно, после занятия переделаю этот момент

from sys import argv

my_arg = argv[1:]
try:
    my_list = list(my_arg)
except:
    my_list = [0, 0, 0]


def my_iterator(source: list) -> int:
    for el in source:
        yield el


my_print_var = list(my_iterator(my_list))
print(my_print_var)