"""
4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""
import math

def f_exp1(x:float,y:float):
    return x ** y

def f_exp2(x:float,y:float):
    return math.exp(y*math.log(x))

def f_exp3(x:float,y:float):
    if y == 0:
        return 1
    elif y > 0:
        ind = 1
        st = 1
        while ind <= y:
            st = st * x
            ind+=1
        return st
    else:
        ind=1
        st=1
        while ind<=abs(y):
            st = st * x
            ind+=1
        return 1 / st


while True:
    a = input('Введите положительное число: ')
    try:
        a = float(a)
    except ValueError:
        print('Вы ввели не число повторите ввод.')
        continue
    if a < 0 or a == 0:
        print('Вы ввели не положительное число повторите ввод.')
        continue
    else:
        break

while True:
    b = input('Введите отрицательное целое число: ')
    try:
        b = float(b)
    except ValueError:
        print('Вы ввели не число, повторите ввод.')
        continue
    if b < 0:
        if b != round(b):
            print('Вы ввели не целое число, повторите ввод.')
            continue
        else:
            break
    else:
        print('Вы ввели не отрицательное число, повторите ввод.')

print("Результат первой функции ",f_exp1(a,b))
print("Результат второй функции ",f_exp2(a,b))
print("Результат третьей функции ",f_exp3(a,b))
