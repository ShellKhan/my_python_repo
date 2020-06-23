my_list = range(20, 241)
result = [el for el in my_list if not (el % 20) or not (el % 21)]
print(result)
