from typing import Callable, Iterable, List
"""
map
zip
round
sum
filter
min
max
abs
sort
reduce
"""

# def my_map(func, some):
#     """
#     Реализация функции map
#     :param func: вызываемая функция
#     :param some: итерируемый объект
#     :return: возвращает список
#     """
#     result = []
#     for itm in some:
#         result.append(func(itm))
#     return result
#
# def my_map2(func: Callable, some: Iterable) -> List:
#     """
#     Реализация функции map
#     :param func: вызываемая функция
#     :param some: итерируемый объект
#     :return: возвращает список
#     """
#     result = []
#     for itm in some:
#         result.append(func(itm))
#     return result
#
# some = ['1', '2']
#
# def some_append(itm, some) -> list:
#     """
#
#     :param itm:
#     :return:
#     """
#     #global some
#     z = some
#     z.append(itm)
#     return z
#
# a = [1,2,3]
# b = my_map(str,a)
# c = my_map(some=a, func=str)
# print(my_map.__doc__)
# print(b)
# print(c)
#
# b = some_append('Hello', a)
# print('a = ',a)
# print('b = ',b)
# print('some = ',some)
#
#
# def some_f(*args, **kwargs):
#     print(type(args))
#     print(args)
#     print(type(kwargs))
#     print(kwargs)
#
# some_f(22,34,56,89,33, key=True, key2=3,key3 = 4)
#
# def my_min(*args):
#     result = float('inf')
#     for itm in args:
#         if result > itm:
#             result = itm
#     return result
#
# def my_min2(*args, key=lambda x: x):
#     result = float('inf')
#     for itm in args:
#         if result > key(itm):
#             result = key(itm)
#     return result
#
# def some_key(x):
#     return x+22*2
#
#
# print(my_min(23,34,762,22,21))
#
# print('min2 = ', my_min2(23,34,762,22,21, key=2))
#
# print(1,2,3,4,sep='---')


def some_temp(template : tuple):
    def producter(items):
        product = {}
        for name, item in zip(template, items):
            product[name] = item
        return product
    return producter

producter_1 = some_temp(('название', 'колво'))
print(producter_1)
a = producter_1(('comp',22))
print(a)

a = [1,2,3,4]
b = [33,45,67,88]
c = [324, 4324, 43243, 433, 323]
print(list(zip(a, b, c)))