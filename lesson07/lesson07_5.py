# Magic metods

import time


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


if __name__ == '__main__':
    hum = Human("Dart", 'Vaider')
    hum2 = Human('Princes', 'Lea')
    hum3 = hum + hum2 # эквивалент hum3 = hum.__add__(hum2)
    a = 1
    b = 2
    c = b.__add__(a)
    print(hum3)
    print(c)