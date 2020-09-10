"""
Задание №1.
Поработайте с переменными, создайте несколько, выведите на экран,
запросите у пользователя несколько чисел и строк и сохраните в переменные,
выведите на экран.
"""

var_int = 43297
var_str = "Hello world!"
var_bool = False
var_float = 3.14

print("Пример натурального числа:", var_int)
print("Пример строки:", var_str)
print("Пример булевой переменной:", var_bool)
print("Пример числа c плавоющей точкой", var_float)

# Ввод произвольного натурального числа
tmp = False #Флаг выхода цикла
while tmp!=True:
    var_int = input("\nВведите натуральное число: ")
    if var_int.isdigit():
        print("Вывод вашего натурального числа:", var_int)
        tmp = True
    else:
        print("Вы ввели не натуральное число, натуральное число это число получаемое при естественном счете N={0,1,2,3,...}, повторите ввод.")

# Ввод произвольной строки, в строке могут быть любые символы
tmp = False #Флаг выхода цикла
while tmp!=True:
    var_str = input("\nВведите строку: ")
    if not var_str:
        print("Вы не чего не ввели в стоку, повторите ввод.")
    else:
        print("Вывод вашей строки: ","\"" ,var_str,"\"",sep='')
        tmp = True

# Ввод булевой переменной
tmp = False #Флаг выхода цикла
while tmp!=True:    # цикл проверки строк ввода булевых переменных
    var_bool = input("\nВведите булевую переменную, пример True или False: ")
    if var_bool == "True" or var_bool == "False":
        if var_bool == "True":
            var_bool = True
            print("Вывод вашей булевой переменной:", var_bool)
        else:
            var_bool = False
            print("Вывод вашей булевой переменной:", var_bool)
        tmp = True
    else:
        print("Вы ввели не правильную булевую переменную, повторите ввод.")

# Ввод числа с плавающей точкой/запятой
tmp = False #Флаг выхода цикла
while tmp!=True:
    var_float = input("\nВведите число с плавающей точкой: ")
    if var_float.isdigit(): #Проверка на целое положительное число или 0
        if int(var_float) == 0: #Проверка на 0
            print("Вы ввели 0, повторите ввод.")
            tmp = False
        else:
            print("Вы ввели целое число, повторите ввод. ")
            tmp = False
    else:
        try:    #Обработка ошибки в случае некорретного перевода введенной строки в число
            float(var_float)
        except ValueError:
            print("Вы ввели число с не плавающей точкой, повторите ввод.")
            tmp = False
            continue # Принудительный повтор цикла
        if float(var_float)>0: # Обрабока если число больше 0
            if float(var_float) != int(float(var_float)): #проверка случая если введено целое число, например 9.0
                var_float = float(var_float)
                print("Вывод вашего числа с плавающей точкой", var_float)
                tmp = True
            else:
                print("Вы ввели целое положительное число, повторите ввод. ")
                tmp = False
        elif float(var_float)<0: # Обрабока если число меньше 0
            if abs(float(var_float)) != abs(int(float(var_float))): # Проверка случая если введено целое отрицательное число, например -9.0
                var_float = float(var_float)
                print("Вывод вашего числа с плавающей точкой", var_float)
                tmp = True
            else:
                print("Вы ввели целое отрицательное число, повторите ввод. ")
                tmp = False
        else:
            print("Вы вывели все равно 0")
            tmp = False



