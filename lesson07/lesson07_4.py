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


if __name__ == '__main__':
    hum = Human("Dart", 'Vaider')
    a = 1
    b = 2
    c = a + b
    print(c)