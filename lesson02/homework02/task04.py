"""
Задание №4.
Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
"""

var_str = input('Введите строку из нескольких слов: ')

var_list = var_str.split(' ')

while var_list.count('')>0: #Цикл очистки списка от пустых значений
    var_list.remove('')

#Вариант 1
print('\nРазбивка по словам')
for ind in range(len(var_list)):
    print(f'{ind+1}. {var_list[ind][:10]}')

#Вариант 2
print('\nРазбивка по словам')
for ind,value in enumerate(var_list,1):
    print(f'{ind}. {value[:10]}')


print("\nДосвидания.")