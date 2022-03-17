import random
class Animal:
    age = 0
    _mass = 2 # _ протектив
    __age = 2 # __ приват, нельзя обращаться
    __population = []
    def __init__(self, a_name, mass):
        self.a_name = a_name
        self.mass = mass
        self.__population.append(self)
    def say(self):
        if self.a_name == 'Пес':
            print('Гав Гав')
        else:
            print('DHSJSHOWHOHNDLSO')
    def get_age(self):
        return self.__age

    def get_population(self):
        return tuple(self.__population)

class Dog(Animal):
    def __init__(self, name):
        self.name = name
        super().__init__('Пес', random.randint(1,3))




animal1 = Animal('Пес', 9)
dog1 = Dog('Фаби')
dog2 = Dog('Лаки')

animal2 = Animal('Кот', 5)
print(animal1._Animal__population)

dog1.say()
print('dddd', dog1.name, dog1.a_name)
print(dog1.get_population())

