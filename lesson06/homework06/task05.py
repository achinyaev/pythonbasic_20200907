"""
Задача №5
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""
class Stationery():
    def draw(self):
        print('Запуск отрисовки')
    def __init__(self, title):
        self.title = title

class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title}')
class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title}')
class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title}')

if __name__ == '__main__':
    cls1 = Pen('Перо')
    cls2 = Pencil('Карандаш')
    cls3 = Handle('Ручка')
    print(cls1.title)
    cls1.draw()
    print(cls2.title)
    cls2.draw()
    print(cls3.title)
    cls3.draw()


