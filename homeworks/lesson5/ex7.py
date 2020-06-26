from statistics import mean
import json
with open('my_text7.txt', encoding='UTF8') as my_file:
    profit_list = []
    firm_list = dict()
    for line in my_file:
        name, form, income, outcome = line.split(' ')
        profit = int(income) - int(outcome)
        if profit > 0:
            profit_list.append(profit)
        firm_list.update({name: profit})
    result = [firm_list, {'average_profit': mean(profit_list)}]

with open('my_text7.json', 'w', encoding='UTF8') as my_res_file:
    json.dump(result, my_res_file)