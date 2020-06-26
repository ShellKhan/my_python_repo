source_file = open('my_text4_1.txt', 'r')
aim_file = open('my_text4_2.txt', 'w', encoding='UTF8')
trans_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
for line in source_file:
    help_list = line.split(' ')
    end_list = []
    for unit in help_list:
        if trans_dict.get(unit):
            end_list.append(trans_dict.get(unit))
        else:
            end_list.append(unit)
    aim_file.write(' '.join(end_list))
source_file.close()
aim_file.close()
