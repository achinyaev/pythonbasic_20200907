"""
Задание №5.
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

"""
rating = [6, 4, 3, 3, 2]
count = 0
position = 0
lenght = 0
res = True

while res!=False:
    print(f"\nРейтинг: {rating}")
    while True:
        var_int = input('Введите новое значение для рейтинга: ')
        if var_int.isdigit():
            var_int = int(var_int)
            break
        else:
            print('Вы ввели некорретное значение.')

    if var_int == 0:
        rating.append(var_int)
    else:
        count = rating.count(var_int)
        if count > 0:
            position = rating.index(var_int)
            rating.insert(position + count, var_int)
        else:
            for position, value in enumerate(rating):
                if var_int > value:
                    rating.insert(position, var_int)
                    break
                elif position < len(rating)-1 and var_int > rating[position + 1]:
                    rating.insert(position+1, var_int)
                    break
                else:
                    rating.append(var_int)
                    break

    print(f"Обновленный рейтинг: {rating}")

    while True:
        tmp = input("\nПоторить ввод Y/N:")
        if tmp in ("N","n"):
            res = False
            break
        elif tmp in ('Y','y'):
            res = True
            break
        else:
            print('Некорректный ввод, повторите.')

print("\nДосвидания.")