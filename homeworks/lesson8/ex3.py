# encoding: utf-8
class NoNumberError(Exception):
    def __init__(self, txt):
        self.txt = txt


def number_check(value: str) -> tuple:
    try:
        convert = int(value)
        return True, convert
    except ValueError:
        try:
            raise NoNumberError('Это не число!')
        except NoNumberError as message:
            return False, message


my_number_list = []
while True:
    pretender = input('Введите число для добавления в список или "q" для окончания ввода: ')
    if pretender == 'q':
        break
    else:
        checker = number_check(pretender)
        if checker[0]:
            my_number_list.append(checker[1])
        else:
            print(checker[1])
print(my_number_list)
