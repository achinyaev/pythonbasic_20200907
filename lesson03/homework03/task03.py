"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
"""

def max_sum(a:float, b:float, c:float):
    if a > b:
        if b > c or b == c:
            return a+b
        else:
            return a+c
    elif a < b:
        if a < c or a == c:
            return b + c
        else:
            return a + b
    else:
        if a > c or a == c:
            return a + b
        else:
            return b+c

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

while True:
    c = input(f'Введите число C: ')
    try:
        c = float(c)
    except ValueError:
        print('Вы ввели не число.')
        continue
    break

print(f'Сумма максимальных двух чисел из набора трех чисел (A,B,C) будет равна {max_sum(a,b,c)}')