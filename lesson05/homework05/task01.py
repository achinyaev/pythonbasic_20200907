"""
Задание 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

if __name__ == '__main__':
    result = ''
    with open('task01.txt', 'w', encoding='UTF-8') as file:
        while True:
            var_str = input("Введите строку: ")
            if not var_str:
                break
            result += var_str + '\n'
        print(result)
        file.write(result)