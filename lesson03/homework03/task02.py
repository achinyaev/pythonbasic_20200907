"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def users1(sep='',**kwargs):
    result = ''
    for key in kwargs:
        result += str(kwargs[key]) + sep
    return result

def users2(name:str,surname,year:int,city:str,email:str,tel:int, sep=''):
    result = ''
    result = name + sep + surname + sep + str(year) + sep + city + sep + email+ sep  + str(tel)
    return result

res = True

while res is True:
    user_template = {
    'name': ('Имя:', str),
    'surname': ('Фамилия:', str),
    'year': ('Год рождения:', int),
    'city': ('Город рождения:', str),
    'email': ('Элетронная почта:', str),
    'tel': ('Номер телефона +7ХХХХХХХХХХ:', int)
    }

    for key, value in user_template.items():
        user_key = {}
        while True:
            user_value = input(f'{value[0]}')
            try:
                user_value = value[1](user_value)
            except ValueError as error:
                print(f'\nВы ввели неверные данные\n{error}')
                continue
            user_template[key] = user_value
            break

    print(users1(sep=' ', **user_template ))
    print(users2(**user_template, sep='-'))

    while True:
        tmp = input("\nПоторить ввод Y/N:")
        if tmp in ("N", "n"):
            res = False
            break
        elif tmp in ('Y', 'y'):
            res = True
            break


