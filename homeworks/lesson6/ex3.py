class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


driver = Position('Иван', 'Иванов', 'водитель', 25000, 5000)
courier = Position('Семен', 'Петров', 'курьер', 15000, 2000)
director = Position('Андрей', 'Дмитриев', 'директор', 100000, 150000)

print(driver.get_full_name())
print(courier.get_total_income())
print(director.name)
print(director.surname)
print(director.position)
print(director._income)
print(director.get_full_name())
print(director.get_total_income())
