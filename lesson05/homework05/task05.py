"""
Задание 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

from random import randint

file_out = 'task05.txt'

if __name__ == '__main__':
    with open(file_out, 'w+',encoding="UTF-8") as file: # Открытие файла в режиме пересоздания с чтением
        file.write(' '.join(map(str,[randint(1, 10) for _ in range(1, 5)]))) # Заполнение файла, интервал случайных чисел и их кол-во можно увеличить
        file.seek(0)    # Переход в начало файла
        # print(file.read())
        # file.seek(0)
        print(f'Сумма чисел в файле = {sum(map(int, file.read().split(" ")))}')
        # sum = 0
        # for item in file.read().split(' '): # Второй вариант через цикл
        #     sum += int(item)

    # print(f'Сумма чисел в файле = {sum}')
