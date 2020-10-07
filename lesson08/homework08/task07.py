"""
Задача №7. 
Реализовать проект «Операции с комплексными числами». 
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел. 
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров. 
Проверьте корректность полученного результата.
"""
class Complex:
    def __init__(self,x,y):
        self.x = float(x)
        self.y = float(y)
    
    def __add__(self, other):
        return Complex(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Complex(self.x - other.x, self.y - other.y)
    
    def __str__(self):
        #return f"Complex={self.x}{'+' if self.y>0 else ''}{str(self.y)+'i' if self.y != 0 '' elif self.y == -1 '-i' elif self.y == 1 '+i'}"
        return f"Complex={self.x}{'+' if self.y>0 else ''}{str(self.y)+'i' if self.y != 0 else ''}"
    def __mul__(self,other):
        return Complex(self.x*other.x-self.y*other.y, self.x*other.y + self.y*other.x)
    
    
if __name__ == '__main__':
    c1 = Complex(3,-5)   # c1 = 3 + 4i
    c2 = Complex(5,-2)  # c2 = 5 - 2i
    print(c1)
    print(c2)
    c3 = c1 + c2
    print(c3)
    c4 = c1 * c2
    print(c4)
    c5 = c1 - c2
    print(c5)