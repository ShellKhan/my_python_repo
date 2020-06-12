# Здесь я для простоты не стал проверять недобросовестный ввод, как в предыдущих заданиях
first_day = int(input("Сколько вы пробежали в первый день? "))
last_day = int(input("Сколько вы хотите пробежать? "))
result = first_day
counter = 1
multiplier = 0.1
while result < last_day:
    counter = counter + 1
    result = result * (multiplier + 1)
print(f"На {counter}-й день вы достигнете результата не менее {last_day} км.")