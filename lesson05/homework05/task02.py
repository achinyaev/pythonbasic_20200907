"""
Задание №2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

if __name__ == '__main__':
    num_str = 0
    with open('task01.txt', 'r', encoding='UTF-8') as file:
        while True:
            st = str.split(file.readline())
            if not st:
                break
            else:
                num_str += 1
                print(f'Строке №{num_str} колво слов = {len(st)}')


