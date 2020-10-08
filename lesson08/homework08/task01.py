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
        ParseDate.parse_date(text)
        self.date = text

    def __str__(self):
        return f'Дата {self.date} {"" if self.check_date(self.date) else "не"}верна'

    @classmethod
    def parse_date(cls, text):
        try:
            cls.__db_result_dates[text] = [int(tmp) for tmp in text.split('-') if tmp.isdigit]
            print(f'Дата разобрана \"{cls.__db_result_dates[text]}\"')
            return True
        except KeyError:
            print(f"Неверный формат данных - {text}, пример коректного ввода: 26-12-1978")
            return False
        except TypeError:
            print(f"Неверный тип данных - {text}, пример коректного ввода: 26-12-1978")
            return False
        except ValueError:
            print(f"Неверный формат даты - {text}, пример коректного ввода: 26-12-1978")
            return False



    @staticmethod
    def check_date(text):
        __mounths_days = [31,28,31,30,31,30,31,31,30,31,30,31]
        try:
            if (0<ParseDate.__db_result_dates[text][2]<3323) and (0<ParseDate.__db_result_dates[text][1]<13) and ParseDate.__db_result_dates[text][0] > 0: # Раз в 3322 года добавляется еще 1 день
                if (ParseDate.__db_result_dates[text][2] % 4 == 0) and (ParseDate.__db_result_dates[text][2] % 100 != 0) or (ParseDate.__db_result_dates[text][2] % 400 == 0):
                    v_year = True
                    if __mounths_days[ParseDate.__db_result_dates[text][1]-1] >= ParseDate.__db_result_dates[text][0]:
                        #print(f'Дата {text} верна 1')
                        return True
                    elif ParseDate.__db_result_dates[text][1] == 2 and __mounths_days[ParseDate.__db_result_dates[text][1]-1] + 1 == ParseDate.__db_result_dates[text][0]:
                        #print(f'Дата {text} верна 2' )
                        return True
                    else:
                        #print(f'В этом месяце не может быть больше {(__mounths_days[ParseDate.__db_result_dates[text][1]-1]+1) if v_year and ParseDate.__db_result_dates[text][1] == 2 else (__mounths_days[ParseDate.__db_result_dates[text][1]-1]) } дней у вас ->{text}')
                        return False
                elif __mounths_days[ParseDate.__db_result_dates[text][1]-1] >= ParseDate.__db_result_dates[text][0]:
                    #print(f'Дата {text} верна 3')
                    return True
                else:
                    #print(f'Дата {text} не верна')
                    return False
            else:
                #print(f'Такая дата {text} не поддерживается')
                return False
        except KeyError:
            return False
            # print(f"Неверный формат даты - {text} ")


if __name__ == '__main__':
    d1 = ParseDate('32-01-1980')
    d2 = ParseDate('31-ff-1f78')
    d3 = ParseDate('12-10-1492')
    d4 = ParseDate('12-04-1961')

    print('\n'+'#' * 80)
    print('Проверка на корректность')
    print("#"*80)

    print(d1)
    print(d2)
    print(d3)
    print(d4)




