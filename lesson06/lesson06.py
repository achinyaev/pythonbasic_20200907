class Animal:
    name = 'SOME NAME'
    age = 0
    _mass = 2 # _ протектив
    __age = 2 # __ приват, нельзя обращаться
    def __init__(self, name, mass):
        print('Start init')
        print(id(self))
        self.name = name
        self.mass = mass
        print('End init')
    def say(self):
        if self.name == 'Пес':
            print('Гав Гав')
        else:
            print('DHSJSHOWHOHNDLSO')
    def get_age(self):
        return self.__age

        # print(f'{self.name} say: DHSJSHOWHOHNDLSO')


animal1 = Animal('Пес', 9)
animal2 = Animal('Кот', 5)
# animal3 = animal1 Зеркалятся обьекты

print(id(animal1),Animal)
print('-'*40)
print(id(animal2),Animal)
animal1.age = 10
animal1.say()

animal1._mass = 1
print(animal1._mass)
