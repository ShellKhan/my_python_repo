secundis = input("Укажите время в секундах: ")
while not secundis.isdigit():
    print('Я просил ввести число')
    secundis = input("Укажите время в секундах: ")
secundis = int(secundis)
minutes = secundis // 60
secundis = secundis % 60
if secundis < 10:
    secundis = '0' + str(secundis)
horas = minutes // 60
minutes = minutes % 60
if minutes < 10:
    minutes = '0' + str(minutes)
if horas < 10:
    horas = '0' + str(horas)
print('Ваше время - %s:%s:%s' % (horas, minutes, secundis))
print('Ваше время - {2}:{1}:{0}'.format(secundis, minutes, horas))
print(f"Ваше время - {horas}:{minutes}:{secundis}")