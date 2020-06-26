# текст в текстовом файле прошу серьезно не воспринимать, он полностью фантастический
import statistics
with open('my_text3.txt', encoding='UTF8') as my_file:
    data_array = []
    for line in my_file:
        unit_name, unit_money = line.split(' ')
        data_array.append({'name': unit_name, 'money': int(unit_money)})

moneys = [el['money'] for el in data_array]
poors = [el['name'] for el in data_array if el['money'] < 20000]
print(poors)
print(statistics.mean(moneys))
