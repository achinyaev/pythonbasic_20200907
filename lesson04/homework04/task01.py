"""
Задание №1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv
def salary(hours:float,bet:float,bonus:float) -> float:
    """
    Расчет зарплаты
    :param hours: отработанные часы
    :param bet: ставка в час
    :param bonus: премия
    :return:
    """
    return hours * bet + bonus

try:
    _, hours, bet, bonus = argv
except ValueError:
    print('Расчет не возможен. Вы ввели неверное колво параметров')
    exit()

for ind, v_arg in enumerate(argv):
    try:
        float(v_arg)
    except ValueError:
        if ind != 0:
            print(f'Ошибка! Параметр №{ind} не число ->',v_arg)
            exit()

print(f'Заработная плата сотрудника = {salary(float(hours), float(bet), float(bonus))}')

