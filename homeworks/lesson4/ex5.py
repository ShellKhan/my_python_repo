def my_mult(data: list) -> int:
    result = 1
    for el in data:
        result *= el
    return result


my_list = [el for el in range(100, 1001) if not (el % 2)]
print(my_list)
print(my_mult(my_list))
