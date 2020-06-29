class Stationery:
    title = 'some kind of stick'

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    title = "pen"

    def draw(self):
        print('Пишем текст.')


class Pencil(Stationery):
    title = "pencil"

    def draw(self):
        print('Чертим чертеж.')


class Handle(Stationery):
    title = "handle"

    def draw(self):
        print('Разрисовываем стену.')


user = Stationery()
writer = Pen()
designer = Pencil()
hooligan = Handle()

print(user.title)
print(writer.title)
print(designer.title)
print(hooligan.title)
user.draw()
writer.draw()
designer.draw()
hooligan.draw()