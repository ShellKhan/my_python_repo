user_list = []
while True:
    user_input = input('Введите число, строку или напишите "хватит": ')
    if user_input == 'хватит':
        break
    user_list.append(user_input)

print('Ваш список:', user_list)

counter = 0
while counter < len(user_list) - 1:
    user_list[counter], user_list[counter + 1] = user_list[counter + 1], user_list[counter]
    counter += 2

print('Список изменен:', user_list)