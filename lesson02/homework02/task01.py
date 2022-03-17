"""
Задание №1.
Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""

var_list = [1, 3, 'Word', 3.14, [100, 1000, 10000], ('a', 'b', 'c'), {1, 4, 6, 8, 9, 10},
            {'key1': 'value1', 'key2': 'value2'},None]

#Вариант решения 1
i = 0
for ind in var_list:
    print(f'Значение элемента списка > {var_list[i]} < его тип: {type(ind)}')
    i += 1

print('\n')
#Вариант решения 2
for ind in var_list:
    print(f'Значение элемента списка > {ind} < его тип: {type(ind)}')

print('\n')
#Вариант решения 3
for ind in range(len(var_list)):
    print(f'Значение элемента списка > {var_list[ind]} < его тип: {type(var_list[ind])}')

print("\nДосвидания.")