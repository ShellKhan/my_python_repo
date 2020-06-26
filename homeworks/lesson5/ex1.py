try:
    my_file = open('my_text1.txt', 'x')
except FileExistsError:
    my_file = open('my_text1.txt', 'w')
while True:
    my_input = input('Введите строку или нажмите Enter для завершения: ')
    if my_input:
        my_file.write(my_input + '\n')
    else:
        my_file.close()
        break
