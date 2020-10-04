"""
Задача №1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
import time
class TraficLight():
    __color = ['Red', 'Yellow', 'Green']
    def running(self, startlight=0):
        count = 0
        while count < 3:
            start = (self.__color.count(startlight) + count) % 3
            if start == 0:
                print(self.__color[start])
                time.sleep(7)
            elif start == 1:
                print(self.__color[start])
                time.sleep(2)
            else:
                print(self. __color[start])
                time.sleep(5)
            count += 1

if __name__ == '__main__':
    tlight = TraficLight()
    tlight.running()
