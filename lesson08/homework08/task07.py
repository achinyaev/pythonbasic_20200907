"""
Задача №7. 
Реализовать проект «Операции с комплексными числами». 
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел. 
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров. 
Проверьте корректность полученного результата.
"""
class Complex:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Complex(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Complex(self.x - other.x, self.y - other.y)
    
    def __mul__(self,other):
        return Complex(self.x*other.x-self.y*other.y, self.x*other.y + self.y*other.x)

    def __str__(self):
        return f"{self.x}{'+' if self.y>0 else '-'}{str(abs(self.y) if abs(self.y) != 1 else '')+'i' if self.y != 0 else ''}"
    
    
if __name__ == '__main__':
    c1 = Complex(3,-5)   # c1 = 3 + 4i
    c2 = Complex(5,-1)   # c2 = 5 - i
    print(f'c1 = {c1}')
    print(f'c2 = {c2}')
    c3 = c1 + c2
    print(f'c3 = {c3}')
    c4 = c1 * c2
    print(f'c4 = {c4}')
    c5 = c1 - c2
    print(f'c5 = {c5}')
