def user_data(name, surname, birthdate, homecity, email, phone):
    """
    Получаем данные пользователя (имя, фамилия, год рождения, город проживания, email, телефон) и выводим их одной строкой
    """
    print(f'Ваше имя {name} {surname}, вы родились в {birthdate} году и живете в городе {homecity}.', end=' ')
    print(f'Ваше мыло {email}, телефон {phone}.')

# Проверяем работу функции
user_data(name='Иван', surname='Петров', birthdate='1999', homecity='Урюпинск', email='111@111.ru', phone='222-223-322')