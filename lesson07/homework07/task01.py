"""
Задание №1. Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка:
сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""
class Matrix():
    def __init__(self, *args):
        self.content = self.fill_matrix(*args)

    def fill_matrix(self, vlist: list):
        m_len = 0
        stat = []
        for key,item in enumerate(vlist):
            stat.append(len(item))
            if stat[key] > m_len:
                m_len = stat[key]

        for key, item in enumerate(stat):
            if m_len > stat[key]:
                for idx in range(0, m_len - stat[key]):
                    vlist[key].append(0)
        return vlist

    def __str__(self):
        indent_size = len(str(max(map(lambda item: max(item, key=lambda x: len(str(x))), self.content)))) + 1
        result = str()
        for line in self.content:
            result += ''.join([f'{item:{indent_size}}' for item in line]) + '\n'
        return result

    def __add__(self, other):
        other_matrix = []
        if len(self.content[0]) == len(other.content[0]) and self.content.__len__() == other.content.__len__():
            # print('Матрицы однотипны')
            for key,item in enumerate(self.content):
                tmp = []
                for idx in range(len(item)-1):
                    tmp.append(self.content[key][idx] + other.content[key][idx])
                other_matrix.append(tmp)
            return Matrix(other_matrix)
        else:
            raise ValueError('Матрицы разные, такое сложение не возможно')



if __name__ == '__main__':
    a = Matrix([[12, 3, 7, 9], [23, 34, 5], [1], [12, 13, 54, 6657, 44]])
    b = Matrix([[32, 8, 7, 9], [23, 34, 5], [4, 5, 89],[10, 13, 54, 457, 44]])
    print(f'Matrix A \n{a.__str__()}',sep='')
    print(f'Matrix B \n{b.__str__()}',sep='')
    c = a + b
    print(f'Matrix C = A + B \n{c.__str__()}',sep='')
    # print(f'Matrix A \n{a.__str__()}\n{b.__str__()}', sep='')

