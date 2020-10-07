"""
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
"""
class MyExcept(Exception):
    def __init__(self, text):
        self.text = text

if __name__ == '__main__':
    v_list = []
    print('\n'+'#'*80+'\n'+'Введите элементы списка'+ '\n' + '#' * 80)

    while True:
        v_str = input("Введите число или 'stop' для завершения: ")
        if v_str == 'stop':
            break
        else:
            try:
                try:
                    v_list.append(float(v_str))
                except ValueError:
                    raise MyExcept('Список может содержать только числа!')
            except MyExcept as err:
                print('>>>', err, '<<<')


    print('\n' + '#' * 80)
    print(f'{"Список пуст" if len(v_list) == 0 else v_list}')