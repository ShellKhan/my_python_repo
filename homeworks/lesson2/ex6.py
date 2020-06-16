goods = []
analitics = {}
params_list = input('Введите список характеристик товара через пробел: ').split(' ')
count = 1

while True:
    dict_hlp = {}
    for param in params_list:
        param_hlp = input('Введите ' + param + ' товара ' + str(count) + ': ')
        dict_hlp[param] = param_hlp
    tuple_hlp = (count, dict_hlp)
    goods.append(tuple_hlp)
    check_more = input('Вводим еще? Введите "да" или "нет": ')
    if check_more == 'нет':
        break
    else:
        count += 1

for param in params_list:
    analitics[param] = []
    for good in goods:
        analitics[param].append(good[1][param])
    analitics[param] = list(set(analitics[param]))

print(goods)
print(analitics)