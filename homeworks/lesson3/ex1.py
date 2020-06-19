def my_divide(arg1, arg2):
    """
    Делим первый аргумент на второй, обрабатывая деление на 0
    """
    if arg2 == 0:
        return 'Нельзя делить на 0!'
    else:
        return arg1 / arg2

# Проверяем работу функции
print(my_divide(4, 2))
print(my_divide(7, 3))
print(my_divide(4, 0))
while True:
    user_input = input('Введите 2 числа, разделенных пробелом или q для завершения программы: ')
    if len(user_input.split(' ')) == 2:
        num1, num2 = user_input.split(' ')
        try:
            print(my_divide(int(num1), int(num2)))
        except ValueError:
            print('Неправильный ввод, попробуйте еще раз')
    elif user_input == 'q':
        break
    else:
        print('Неправильный ввод, попробуйте еще раз')
