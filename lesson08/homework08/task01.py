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
    def parse_date(cls, text):
        try:
            cls.__db_result_dates[text] = [int(tmp) for tmp in text.split('-') if tmp.isdigit]
            print(f'Дата разобрана \"{cls.__db_result_dates[text]}\"')
            return cls.__db_result_dates[text]
        except KeyError:
            print(f"Неверный формат данных - {text}, пример коректного ввода: 26-12-1978")
        except TypeError:
            print(f"Неверный тип данных - {text}, пример коректного ввода: 26-12-1978")
        except ValueError:
            print(f"Неверный формат даты - {text}, пример коректного ввода: 26-12-1978")



    @staticmethod
    def check_date(text):
        __mounths_days = [31,28,31,30,31,30,31,31,30,31,30,31]
        try:
            if (0<ParseDate.__db_result_dates[text][2]<3323) and (0<ParseDate.__db_result_dates[text][1]<13) and ParseDate.__db_result_dates[text][0] > 0: # Раз в 3322 года добавляется еще 1 день
                if (ParseDate.__db_result_dates[text][2] % 4 == 0) and (ParseDate.__db_result_dates[text][2] % 100 != 0) or (ParseDate.__db_result_dates[text][2] % 400 == 0):
                    if __mounths_days[ParseDate.__db_result_dates[text][1]-1] >= ParseDate.__db_result_dates[text][0]:
                        print(f'Дата {text} верна')
                        return True
                    elif ParseDate.__db_result_dates[text][1] == 2 and __mounths_days[ParseDate.__db_result_dates[text][1]-1] + 1 == ParseDate.__db_result_dates[text][0]:
                        print(f'Дата {text} верна')
                        return True
                    else:
                        print(f'В феврале не может быть больше 29 дней у вас ->{text}')
                        return False
                elif __mounths_days[ParseDate.__db_result_dates[text][1]-1] >= ParseDate.__db_result_dates[text][0]:
                    print(f'Дата {text} верна')
                    return True
                else:
                    print(f'Дата {text} не верна')
                    return False
            else:
                print(f'Такая дата {text} не поддерживается')
                return False
        except KeyError:
            print(f"{text} - Неверный формат даты")


if __name__ == '__main__':
    d1 = ParseDate('31-02-1976')
    d2 = ParseDate('31-ff-1f78')
    print('\n'+'#' * 80)
    print(f'Обработка {d1.date}')
    d1.parse_date(d1.date)

    print('\n'+'#' * 80)
    print(f'Обработка {d2.date}')
    d2.parse_date(d2.date)

    print('\n'+'#' * 80)
    print('Проверка на корректность')
    d1.check_date(d1.date)
    d2.check_date(d2.date)
    print(ParseDate())


