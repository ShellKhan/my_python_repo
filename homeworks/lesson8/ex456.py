# encoding: utf-8
"""
Тут решения задач 4, 5 и 6 вместе. Я немножко упростился, так как не смог придумать связный пример для каких-то
уникальных характеристик классов - просто сделал словарь для любых вообще характеристик кроме типа.
Зато учет сделал индивидуализированным - каждый экземпляр можно поименовать и потом найти по имени.
Также сделал поиск по типу - если такое имеется, выводится количество.
С пользовательским вводом маленько поленился (если это очень надо, доделаю, но мы же его кучу раз уже делали,
так что это, уж извините, скучно).
А вместо того прикрутил проверку на наличие техники, отправляемой на другой склад - если чего-то не хватает,
отправляется только найденное и выводится отчет, чего именно не нашлось.
"""


class Equip:
    type = ''

    def __init__(self, params):
        self.params = params

    def __str__(self):
        return self.type + ' ' + self.params['name']


class Printer(Equip):
    type = 'printer'


class Scanner(Equip):
    type = 'scanner'


class Copier(Equip):
    type = 'copier'


class Plotter(Equip):
    type = 'plotter'


class Warehouse:
    NO_ITEM_WARNING = '\nна этом складе нет такой единицы оргтехники'
    avail = {}
    quantity = {}

    def __init__(self, name):
        self.name = name

    def __str__(self):
        result = []
        for key in self.avail.keys():
            valuestr = []
            for el in self.avail[key]:
                valuestr.append(str(el))
            result.append(str((key, self.quantity[key], valuestr)))
        return '\n' + '\n'.join(result)

    def add_items(self, items_list):
        for unit in items_list:
            if unit.type not in self.avail.keys():
                self.avail[unit.type] = [unit]
            else:
                self.avail[unit.type].append(unit)
            self.quantity[unit.type] = len(self.avail[unit.type])
        print(self)

    def remove_items(self, items_list):
        success = []
        errors = []
        for unit in items_list:
            try:
                self.avail[unit.type].remove(unit)
                self.quantity[unit.type] = len(self.avail[unit.type])
                success.append(unit)
            except ValueError:
                errors.append(str(unit))
                print(self.NO_ITEM_WARNING + ' - ' + str(unit))
        return {'success': success, 'errors': errors}

    def move_to_filial(self, item_list, filial):
        report = self.remove_items(item_list)
        filial.add_items(report['success'])
        print(f'\nУспешно передано:\n{[str(unit) for unit in report["success"]]}')
        print(f'\nНе найдено на складе:\n{report["errors"]}')

    def search_by(self, type, name=''):
        if type in self.avail.keys():
            if not name:
                return f'\nНа этом складе есть {str(self.quantity[type])} {type}'
            else:
                for item in self.avail[type]:
                    if item.params['name'] == name:
                        return f'\n{type} {name} обнаружен на этом складе'
                return f'\nНа этом складе нет {type} {name}'
        else:
            return f'\nНа этом складе нет {type}'


msk_war = Warehouse('Moscow')
spb_war = Warehouse('Sankt-Peterburg')

old_lamp_plotter = Plotter({'age': 'old', 'color': 'white', 'made_in': 'USSR', 'name': 'старый ламповый плоттер'})
new_laser_printer = Printer({'age': 'new', 'method': 'laser', 'made_in': 'China', 'name': 'новый лазерный принтер'})
japan_scanner = Scanner({'made_in': 'Japan', 'name': 'японский сканер'})
german_scanner = Scanner({'made_in': 'Germany', 'name': 'немецкий сканер'})
old_matrix_printer = Printer({'age': 'old', 'made_in': 'Japan', 'method': 'matrix', 'name': 'старый матричный принтер'})

msk_war.add_items([old_lamp_plotter, new_laser_printer, old_matrix_printer, german_scanner])
msk_war.move_to_filial([old_lamp_plotter, old_matrix_printer, japan_scanner], spb_war)

print(spb_war.search_by('plotter'))
print(msk_war.search_by('copier'))
print(msk_war.search_by('printer', 'новый лазерный принтер'))
print(msk_war.search_by('scanner', 'японский сканер'))
