# Magic metods

import time

class GarageIter:
    def __init__(self, box):
        self.__idx = 0
        self.__box = box

    def __next__(self):

        while self.__idx < len(self.__box):
            self.__idx += 1
            return self.__box[self.__idx - 1]

        raise StopIteration


class Human:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __del__(self):
        print('Я твой отец')

    def __str__(self):
        return f'{self.name} {self.surname}'

    def __add__(self, other):
        return  type(self)(other.name, self.surname)

class Garage:
    def __init__(self, name):
        self.name = name
        self.__box = []

    def set_car(self, car):
        self.__box.append(car)

    def  __getitem__(self, item):
        return self.__box[item]

    def __iter__(self):
        return GarageIter(self.__box)
       # return self.__box__iter__()


class Car():
    def __init__(self, name, vin=None):
        self.name = name
        self.vin = vin


if __name__ == '__main__':
    garage = Garage('Crazy Monkey')
    car1 = Car('Ford',342234525)
    car2 = Car('GMC',874703473)
    car3 = Car('Toyota',556234577)

    garage.set_car(car1)
    garage.set_car(car2)
    garage.set_car(car3)

    for car in garage:
        print(car)

    print(garage[0])