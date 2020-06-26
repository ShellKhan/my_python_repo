# делать тупо набор готовых чисел показалось скучным,
# поэтому я автоматически генерирую последовательность случайных цифр и пробелов.
# числа извлекаются сплитом по пробелу,
# пустые строки между сдвоенными пробелами отбрасываются
import random
aim_file = open('my_text5.txt', 'w+')
counter = 50
result = []
while counter:
    result.append(random.choice('0123456789   '))
    counter -= 1
aim_file.write(''.join(result))
aim_file.seek(0)
num_list = [int(el) for el in aim_file.read().split(' ') if el]
aim_file.close()
print(sum(num_list))
