# Magic metods

import time

class Human:
    def __init__(self, name, surname):
        self.name = name


    def __del__(self):
        print('Я таю')

if __name__ == '__main__':
    some = Some()

    print('.')

    del some

    for num in range(1000):
        print(num)
        time.sleep(1)
        if num > 10:
            print(some)

