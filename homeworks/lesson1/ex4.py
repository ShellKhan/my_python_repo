no_input = True
while no_input:
    user_num = input("Введите целое положительное число: ")
    if not user_num.isdigit():
        print('Это не число!')
    else:
        user_num = int(user_num)
        if user_num == 0:
            print('Это ноль, а не положительное число!')
        else:
            no_input = False
user_last_digit = user_num % 10
user_answer = user_last_digit
while user_last_digit != user_num:
    user_num = user_num // 10
    user_last_digit = user_num % 10
    if user_last_digit > user_answer:
        user_answer = user_last_digit
print(f'Ваша самая большая цифра - {user_answer}')