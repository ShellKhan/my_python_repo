user_num = input("Введите число: ")
while not user_num.isdigit():
    user_num = input("Это не число.\nВведите число: ")
user_num = int(user_num)
user_result = user_num + user_num * 11 + user_num * 111
print(user_result)

