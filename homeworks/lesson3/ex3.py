def my_func(arg1, arg2, arg3):
    """
    принимаем три аргумента и отдаем сумму наибольших двух из них
    """
    maxarg1 = max(arg1, arg2)
    maxarg2 = max(arg1, arg3)
    maxarg3 = max(arg2, arg3)
    return sum(list({maxarg1, maxarg2, maxarg3}))

# Проверяем работу функции
print(my_func(1, 2, 5))
print(my_func(111, 22, 5))
print(my_func(10, 10, 50))