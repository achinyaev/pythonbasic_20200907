"""
Задание №7.
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

from json import dump,dumps

file_in = 'task07.txt'
file_out = 'task07.json'

db_companies = []
reestr = {}
loosers = {}
profit = {}
summ = 0

if __name__ == '__main__':
    with open(file_in,'r',encoding='UTF-8') as file:
        print('Содержимое файла:')
        print('-'*40)
        for line in file.readlines():
            print(line, end='')
            tmp = line.split()
            if float(tmp[2]) > float(tmp[3]) or float(tmp[2]) == float(tmp[3]):
                reestr[tmp[0]] = float(tmp[2]) - float(tmp[3])
                summ += reestr[tmp[0]]
            else:
                loosers[tmp[0]] = float(tmp[2]) - float(tmp[3])
        if reestr.__len__():
            db_companies.append(reestr)
        profit['average_profit'] = summ / reestr.__len__()
        db_companies.append(profit)
        if loosers.__len__():
            db_companies.append(loosers)
        print('-' * 40)
        print('DB Companies ->', db_companies)


    with open(file_out , 'w', encoding="UTF-8") as file: # Запись в JSON файл
        dump(db_companies, file, ensure_ascii=False)

    print(f'JSON Data ->', dumps(db_companies, ensure_ascii=False))


