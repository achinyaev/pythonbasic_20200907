"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""

def summa(arg:float):
    global sum
    sum += arg

sum = 0
res = True

while res is True:
    tmp = input('Введите цифры разделенные пробелом ')
    tmp = tmp.split(' ')
    tmp = list(filter(None,tmp)) #Удаление лишних пробелов, можно этого не делать если считать второй и боллее пробел спец.символом
    for value in tmp:
        try:
            value = float(value)
        except ValueError:
            res = False
            break
        summa(value)

    print("Сумма введенных чисел = ", sum)

    while True and res is True:
        tmp = input("\nПоторить ввод чисел, Y/N:")
        if tmp in ("N", "n"):
            res = False
            break
        elif tmp in ('Y', 'y'):
            res = True
            break