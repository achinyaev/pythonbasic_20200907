"""
Задача №4.
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево).
А также методы:
go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).

Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""

class Car():
    def __init__(self, speed, color, name, is_police = False):
        """
        :param speed: this number
        :param color: this str for example 'Red', 'White', etc.
        :param name: this str for example 'Corolla', 'Mark 2', 'Chaser', etc.
        :param is_police: this boolean for example: True or False
        """
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print(f'Машина поехала, со скоростью {self.speed}')

    def stop(self):
        print(f'Машина отсановилась')

    def turn(self, direction):
        """
        :param direction: value "Left" or "Right"
        :return:
        """
        self.direction = {'Left': 'налево', 'Right': 'направо'}
        print(f'Машина повернула {self.direction[str.title(direction)]}')
    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.speed}')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60 and self.is_police is not True:
            print(f'Вы привысили разрешенную скорость автомоибиля на {self.speed - 60} километров в секунду')
        else:
            print(f'Текущая скорость автомобиля {self.speed}')

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40 and self.is_police is not True:
            print(f'Вы привысили разрешенную скорость автомоибиля на {self.speed - 40} километров в секунду')
        else:
            print(f'Текущая скорость автомобиля {self.speed}')

class SportCar(Car):
    pass

class PoliceCar(Car):
    def __init__(self):
        self.is_police = True

if __name__ == '__main__':
    car1 = Car(100, 'Red', 'Mark2', 0)
    car1.go()
    car1.stop()
    car1.turn('left')

    car2 = TownCar(90, 'Red', 'Corolla', True)
    print(car2.is_police)
    car2.show_speed()
    car3 = SportCar(150,'Black','Mark II',False)
    car3.show_speed()
    car3.go()
    car3.turn('left')


