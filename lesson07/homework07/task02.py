"""
Задача №2.
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class Clothes(ABC):

    @property
    @abstractmethod
    def consumption(self):
        pass

    @property
    @abstractmethod
    def params(self):
        pass


class Suit(Clothes):

    def __init__(self, name: str, height: float):
        self.__height = height
        self.name = name

    @property
    def consumption(self):
        return 2 * self.__height + 0.3

    @property
    def params(self):
        return self.__height


class Coat(Clothes):
    def __init__(self, name: str, size: float):
        self.name = name
        self.__size = size

    @property
    def consumption(self):
        return self.__size / 6.5 + 0.5

    @property
    def params(self):
        return self.__size

if __name__ == '__main__':
    coat1 = Coat('Пальто драповое', 52)
    suit1 = Suit('Костюм деловой', 1.80)
    print(f'На \'{coat1.name}\' для размера {coat1.params} уйдет {coat1.consumption} метров ткани')
    print(f'На \'{suit1.name}\' для роста {suit1.params*100}cм уйдет {suit1.consumption} метров ткани')