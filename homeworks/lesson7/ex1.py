# encoding: utf-8
class Matrix:
    """ Этот класс создает двумерную матрицу из списка списков values.
    Списки-элементы списка списков должны быть одинаковой длины.
    """
    field = []
    rows = 0
    cols = 0

    def __init__(self, source_list: list):
        if self.check_arg(source_list):
            self.rows = len(source_list)
            self.cols = self.check_size_cols(source_list)
            self.field = source_list
        else:
            raise TypeError('Аргумент должен быть списком списков!')

    @staticmethod
    def check_arg(data: list) -> bool:
        if not isinstance(data, list):
            return False
        else:
            for el in data:
                if not isinstance(el, list):
                    return False
            return True

    @staticmethod
    def check_size_cols(checked_list: list) -> int:
        colsize = {len(el) for el in checked_list}
        if len(colsize) > 1:
            raise ValueError('Строки в матрице неравной длины!')
        else:
            return colsize.pop()

    def __str__(self) -> str:
        return '{\n' + ',\n'.join([', '.join([str(el) for el in line]) for line in self.field]) + '\n}'

    def __add__(self, other: 'Matrix') -> 'Matrix':
        if not isinstance(other, Matrix):
            raise TypeError('Матрицу можно складывать только с матрицей!')
        elif self.rows != other.rows or self.cols != other.cols:
            raise ValueError('Складывать можно только матрицы одинакового размера!')
        else:
            return Matrix([[(self.field[row][col] + other.field[row][col])
                            for col in range(self.cols)] for row in range(self.rows)])


ex1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
ex2 = Matrix([[2, 4, 6], [8, 10, 12], [14, 16, 18]])
ex3 = ex1 + ex2
print(ex3)
