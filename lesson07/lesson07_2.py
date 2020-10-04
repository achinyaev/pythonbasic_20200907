

class Speed:
    __slot__ = ('kmph',) # Задаются какие могут быть переменные
    def __init__(self):
        self.kmph = 0

    @property
    def meter_sec(self):
        return self.kmph / 3.6

    @meter_sec.setter
    def meter_sec(self, value: float):
        self.kmph  = value * 3.6

    @property
    def mph(self):
        return self.kmph / 1.609

    @mph.setter
    def mph(self, value: float):
        self.kmph = value * 1.609

if __name__ == '__main__':
    speed = Speed()
    speed.kmph = 100
    speed.meter_sec = 40
    print('.')
