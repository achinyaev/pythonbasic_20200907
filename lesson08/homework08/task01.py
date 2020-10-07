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
        except TypeError as err:
            print("Неверный формат данных ")
        except ValueError as err:
            print("Неверный формат данных ")
        return cls.__db_result_dates

    @staticmethod
    def check_date(text):
        __mounths = [31,28,31,30,31,30,31,31,30,31,30,31]
        try:
            if (0<ParseDate.__db_result_dates[text][2]<3323) and (0<ParseDate.__db_result_dates[text][1]<13) and ParseDate.__db_result_dates[text][0] > 0: # Раз в 3322 года добавляется еще 1 день
                if (ParseDate.__db_result_dates[text][2] % 4 == 0) and (ParseDate.__db_result_dates[text][2] % 100 != 0) or (ParseDate.__db_result_dates[text][2] % 400 == 0): 
                    if __mounths[ParseDate.__db_result_dates[text][1]-1] >= ParseDate.__db_result_dates[text][0]:
                        return True
                    elif ParseDate.__db_result_dates[text][1] == 2 and __mounths[ParseDate.__db_result_dates[text][1]-1] + 1 == ParseDate.__db_result_dates[text][0]:
                        return True
                    else:
                        return False
                elif __mounths[ParseDate.__db_result_dates[text][1]-1] >= ParseDate.__db_result_dates[text][0]:
                    return True
                else:
                    return False
            else:
                print('Такая дата не поддерживается')
                return False
        except IndexError:
            return False
        except AttributeError:
            return False
        except KeyError:
            return False
    

if __name__ == '__main__':
    datestamp1 = '31-02-1976'
    d1 = ParseDate(datestamp1)
    d1.parse_date()
    d1.check_date(datestamp1)


