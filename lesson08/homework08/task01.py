"""
Задача №1.
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""
class ParseDate:
    __db_dates = []
    __db_result_dates = {}
    def __init__(self, text):
        ParseDate.__db_dates.append(text)
        self.date = text

    @classmethod
    def parse_date(cls):
        try:
            for item in cls.__db_dates:
                cls.__db_result_dates[item] = [int(tmp) for tmp in item.split('-') if tmp.isdigit]
            return cls.__db_result_dates
        except TypeError:
            print(f'Неверный формат данных')

    @staticmethod
    def check_date(text):
        try:
            if (0<ParseDate.__db_result_dates[text][2]<3322) and (0<ParseDate.__db_result_dates[text][1]<13) and (0<ParseDate.__db_result_dates[text][0]<32):
                if not (ParseDate.__db_result_dates[text][2] % 4):
                    if  (ParseDate.__db_result_dates[text][2] % 400 or ParseDate.__db_result_dates[text][2] % 100):
                        print('Год невысокосный 1 ')
                        year = True
                    else:
                        print('Год высокосный 2')
                        year = True
                else:
                    print('Год невысокосный 3')
            else:
                print('Такая дата не поддерживается')

        except IndexError:
            return False
        except AttributeError:
            return False



if __name__ == '__main__':
    d1 = ParseDate('12-12-2020')
    d1.parse_date()
    d1.check_date('12-12-2020')


