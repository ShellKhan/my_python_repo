from sys import argv

try:
    my_start = int(argv[1])
except:
    my_start = 0
try:
    my_end = int(argv[2])
except:
    my_end = my_start + 10
if my_start > my_end:
    my_end, my_start = my_start, my_end


def my_iterator(start: int, end: int) -> int:
    for el in range(start, end + 1):
        yield el


my_print_var = list(my_iterator(my_start, my_end))
print(my_print_var)
