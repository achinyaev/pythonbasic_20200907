"""
Задание №6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
"""
from itertools import count, cycle
from sys import argv

try:
    _, num, vlist = argv
except ValueError:
    print(f'Вы ввели неверное кол-во параметров. \nВведите: целое_число и список_через_запятую \nПример: {argv[0]} 21 1,4,6,9,13\n')
    exit()

try:
    num = int(num)
except ValueError:
    print('Первый аргумент должен быть целым числом')
    exit()

vlist = vlist.split(',')

print(f'Итератор A от числа {num} ->', end=' ')
for item in count(num):
    if item > num+10:
        break
    else:
        print(item, end=' ')


print(f'\nИтератор B по списку {vlist} ->', end=' ')
ind = 0
for item in cycle(vlist):
    if ind > 10:
        break
    print(item, end=' ')
    ind += 1
