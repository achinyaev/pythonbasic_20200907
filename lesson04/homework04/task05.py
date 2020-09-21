"""
Задание №5.
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""
from functools import reduce

def multic(a:float,b:float) -> float:
    """
    Функция умножения
    :param a: аргумент float
    :param b: аргумент float
    :return: результат float
    """
    return a * b

var_list = [item for item in range(100,1001) if not item & 1]

print(var_list)
print(reduce(multic,var_list))