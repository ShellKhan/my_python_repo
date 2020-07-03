# encoding: utf-8
from abc import ABC, abstractmethod


class Clothes(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def size(self) -> str:
        pass

    @abstractmethod
    def consumption(self) -> float:
        pass


class Coat(Clothes):
    name = 'пальто'
    size_name = 'размер'
    size = 0
    __quantity = 0
    __common_consumption = 0

    def __init__(self, size):
        self.size = size
        Coat.__quantity += 1
        Coat.__common_consumption += self.consumption()

    def __str__(self) -> str:
        return self.name + ' ' + str(self.size) + ' ' + self.size_name + 'а'

    def consumption(self) -> float:
        return self.size / 6.5 + 0.5

    @staticmethod
    def common_consumption():
        return round(float(Coat.__common_consumption), 2)


class Suit(Clothes):
    name = 'костюм'
    size_name = 'рост'
    size = 0
    __quantity = 0
    __common_consumption = 0

    def __init__(self, size):
        self.size = size
        Suit.__quantity += 1
        Suit.__common_consumption += self.consumption()

    def __str__(self) -> str:
        return self.name + ' ' + str(self.size) + ' ' + self.size_name + 'а'

    def consumption(self) -> float:
        return 2 * self.size + 0.3

    @staticmethod
    def common_consumption():
        return round(float(Suit.__common_consumption), 2)


coat1 = Coat(42)
coat2 = Coat(48)
suit1 = Suit(23)
suit2 = Suit(25)
suit3 = Suit(27)
print(coat1)
print(coat2)
print(suit1)
print(suit2)
print(suit3)
print('Общий расход ткани - ' + str(Coat.common_consumption() + Suit.common_consumption()))
