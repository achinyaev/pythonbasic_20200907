"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""

def fdel(a,b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = False
        print('Ошибка деление на 0.')
    return result

while True:
    a = input(f'Введите число А: ')
    try:
        a = float(a)
    except ValueError:
        print('Вы ввели не число.')
        continue
    break

while True:
    b = input(f'Введите число B: ')
    try:
        b = float(b)
    except ValueError:
        print('Вы ввели не число.')
        continue
    break

res = fdel(a,b)

if res != False:
    print(f'A/B = {res}')



