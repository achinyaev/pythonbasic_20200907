"""
Задача №2.
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

class MyExcept(ZeroDivisionError):
    def __init__(self, text):
        self.text = text

if __name__ == '__main__':
    print('Введите последовательно два числа')
    num1 = input('Ввведите число, делимое  ')
    num2 = input('Ввведите число, делитель  ')

    try:
        num1 = int(num1)
        num2 = int(num2)
        if num2 == 0:
            raise MyExcept('Делить на 0 нельзя')
        result = num1 / num2
    except ValueError:
        print('Вы ввели не число')
    except MyExcept as err:
        print(err)
    else:
        print(f"Частное от деления {num1}/{num2} = {result}")





