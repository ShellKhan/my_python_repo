def my_func(idx: int) -> bool:
    return (my_list[idx] > my_list[idx - 1])


my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [my_list[idx] for idx in range(1, len(my_list)) if my_func(idx)]
print(result)
