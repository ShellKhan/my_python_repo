# процедура уязвима к формату записи
# случайный пробел между числом и пояснением в скобках или другой символ для прочерка всё ломают
# но я не стал изобретать тут решения, так как по хорошему надо бы использовать регэкспы,
# а мы их еще не учили (а они вообще в питоне есть?)
with open('my_text6.txt', encoding='UTF8') as my_file:
    my_dict = dict()
    for line in my_file:
        name, *hours = line.split(' ')
        name = name.replace(':','')
        hour_sum = sum([int(el.split('(')[0]) for el in hours if el[0:1] != '-'])
        my_dict.update({name: hour_sum})
    print(my_dict)
