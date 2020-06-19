# Здесь я для простоты не стал проверять недобросовестный ввод, как в предыдущих заданиях
user_income = int(input("Какова выручка вашей фирмы? "))
user_outcome = int(input("Каковы издержки вашей фирмы? "))
if user_income > user_outcome:
    print("Вы работаете с прибылью")
    user_rent = (user_income - user_outcome) / user_income
    user_size = int(input("А сколько у вас сотрудников? "))
    user_rent_per_unit = user_rent / user_size
    print(f"Каждый ваш сотрудник приносит {user_rent_per_unit} прибыли")
elif user_income == user_outcome:
    print("Вы выходите в ноль")
else:
    print("Вы работаете в убыток")

