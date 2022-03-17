"""
Задание №2.
Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""



var_list1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
var_list2 = [var_list1[item] for item in range(1,len(var_list1)-1) if var_list1[item] > var_list1 [item-1]]

print("Исходный список", var_list1)
print("Результирующий список", var_list2)