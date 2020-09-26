"""
Задание №3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
"""

if __name__ == '__main__':
    with open('task03.txt', 'r', encoding='UTF-8') as file:
        context = file.readlines()

    fund = 0

    for line,item in enumerate(context):
        try:
            if float(item.split()[1]) < 20000:
                print(f'У сотрудника с фамилией {item.split()[0]} зарплата меньше 20т.р. и равна = {float(item.split()[1]):.2f}')
        except ValueError:
            print("Не корректные значения в файле. Программа завершается.")
            exit()
        fund += float(item.split()[1])

    print(f"Средняя зарплата по компании = {fund/(line+1):.2f}")