# encoding: utf-8
class Complex:
    real_part = 0
    imaginary_part = 0

    def __init__(self, real_p, imag_p):
        self.real_part = real_p
        self.imaginary_part = imag_p

    def __add__(self, other):  # (a + bi) + (c + di) = (a + c) + (b + d)i
        return Complex(self.real_part + other.real_part, self.imaginary_part + other.imaginary_part)

    def __mul__(self, other):  # (a + bi) * (c + di) = (ac - bd) + (bc + ad)i
        ac = self.real_part * other.real_part
        bd = self.imaginary_part * other.imaginary_part
        bc = self.imaginary_part * other.real_part
        ad = self.real_part * other.imaginary_part
        return Complex(ac - bd, bc + ad)

    def __str__(self):
        return f'{self.real_part} + {self.imaginary_part}i'


tst1 = Complex(11, 8)
tst2 = Complex(2, 5)
tst3 = tst1 + tst2
tst4 = tst1 * tst2

print(tst1)
print(tst2)
print(tst3)
print(tst4)
