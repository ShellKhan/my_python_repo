def my_func(x, y):
    """
    Возведение в отрицательную степень
    :param x: float
    :param y: int < 0
    :return: float
    """
    # первый рекомендованный способ испытал и закомментировал:
    # return x ** y
    y = -y
    pow_x = 1
    while y:
        pow_x /= x
        y -= 1
    return pow_x

# Проверяем работу функции

print(my_func(2, -2))
print(my_func(5, -2))
print(my_func(10, -4))
print(my_func(7.256, -2))
