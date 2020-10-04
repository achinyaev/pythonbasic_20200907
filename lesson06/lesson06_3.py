import random

NAMES = ('Шарик', "Бобик", "Пират")

class Animal:
    age = 0
    _mass = 2 # _ протектив
    __age = 2 # __ приват, нельзя обращаться
    __population = []
    def __init__(self, a_type, mass):
        self.a_type = a_type
        self.mass = mass
        self.__population.append(self)
    def say(self):
        print('DHSJSHOWHOHNDLSO')

    def get_age(self):
        return self.__age

    def get_population(self):
        return tuple(self.__population)

    def breeding(self, other):
        cls = random.choice((type(self), type(other)))
        return cls(self.a_type, random.randint(1,4))

class Dog(Animal):
    def __init__(self, name):
        self.name = name
        super().__init__('Пес', random.randint(1,3))

    def say(self):
        print('Гав Гав')

    def breeding(self, other):
        cls = random.choice((type(self), type(other)))
        return cls(random.choice(NAMES))

class Cat(Animal):
    def __init__(self, name):
        self.name = name
        super().__init__('Кошка', random.randint(1,3))

    def say(self):
        super().say() #вызов метод родителя
        print('Мяю Мяю')


class Zoo:
    def __init__(self, name):
        self.name = name
        self.__animals = {}

    def add_animal(self, animal):
        if self.__animals.get(animal.a_type):
            self.__animals.get(animal.a_type).append(animal)
        else:
            self.__animals[animal.a_type] = [animal]

    def atype_population(self,atype):
        return self.__animals.get(atype)


zoo = Zoo('Спб')



# 2:15 стало непонятно



animal1 = Animal('Пес', 9)
dog1 = Dog('Фаби')
dog2 = Dog('Лаки')
zoo.add_animal(dog1)
zoo.add_animal(dog2)
animal2 = Animal('Кот', 5)
print(animal1._Animal__population)
zoo.add_animal(animal2)

dog1.say()
print('dddd', dog1.name, dog1.a_type)
print(dog1.get_population())

cat1 = Cat('Коржик')
cat2 = Cat('Груня')
zoo.add_animal(cat1)
zoo.add_animal(cat2)
cat2.say()

print('--'*20)

animal3 = animal1.breeding(animal2)
print(animal3.a_type)

dog3 = Dog("Шар")

print(dog3.a_type)
print(dog3.name)

zoo.add_animal(animal1)
