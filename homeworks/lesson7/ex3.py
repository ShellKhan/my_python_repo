# encoding: utf-8
class Cell:
    NOT_CELLS_ERROR = 'Для этой операции требуются две клетки.'
    NOT_ENOUGH_UNITS = 'Операция невозможна: в результате нет ячеек.'

    def __init__(self, units):
        self.units = units

    def __add__(self, other):
        if type(other) != Cell:
            raise TypeError(NOT_CELLS_ERROR)
        return Cell(self.units + other.units)

    def __sub__(self, other):
        if type(other) != Cell:
            raise TypeError(NOT_CELLS_ERROR)
        if self.units <= other.units:
            raise ValueError(NOT_ENOUGH_UNITS)
        return Cell(self.units - other.units)

    def __mul__(self, other):
        if type(other) != Cell:
            raise TypeError(NOT_CELLS_ERROR)
        return Cell(self.units * other.units)

    def __truediv__(self, other):
        if type(other) != Cell:
            raise TypeError(NOT_CELLS_ERROR)
        if not self.units // other.units:
            raise ValueError(NOT_ENOUGH_UNITS)
        return Cell(self.units // other.units)

    def make_order(self, length):
        return ''.join(['*' + ('\n' * (not (num + 1) % length) * (num != self.units - 1)) for num in range(self.units)])


cell1 = Cell(15)
cell2 = Cell(10)
cell3 = Cell(5)
cell4 = Cell(12)
cell5 = Cell(13)

sum = cell1 + cell2
sub = cell1 - cell3
mul = cell3 * cell4
div = cell5 / cell4

print(sum.make_order(5))
print(sub.make_order(3))
print(mul.make_order(12))
print(div.make_order(5))
