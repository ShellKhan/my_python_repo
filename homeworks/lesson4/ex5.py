from functools import reduce as my_red


def my_mult(prev_el: int, el: int) -> int:
    return prev_el * el


my_list = my_red(my_mult, [el for el in range(100, 1001, 2)])
print(my_list)
