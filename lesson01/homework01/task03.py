"""
Задание №3.
Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""

tmp = False # Временная переменная, флаг для цикла
while tmp!=True:    #Цикл проверки целого положительного числа
    var_int = input("\nВведите целое положительно число n: ")
    if var_int.isdigit():
        if int(var_int)>0:
            tmp = True
        else:
            print("Число не должно равняться 0")
    else:
        print("Вы ввели не целое число, повторите ввод.")

print("Сумма чисел %s+%s+%s" % (var_int, var_int+var_int, var_int+var_int+var_int),"=",int(var_int)+int(var_int+var_int)+int(var_int+var_int+var_int))

