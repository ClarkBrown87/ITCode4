import math


class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def plus(self):
        return self.a + self.b

    def minus(self):
        return self.a - self.b

    def split(self):
        if self.b == 0:
            return 'На 0 делить нельзя'
        else:
            return self.a / self.b

    def multiply(self):
        return self.a * self.b

    def my_pow(self):
        return pow(self.a, self.b)

    def squared(self, x=0):
        if x == 0:
            return self.a ** 2
        else:
            return self.b ** 2


calc = Calculator(2, 3)
print(f'Плюс = {calc.plus()}')
print(f'Минус = {calc.minus()}')
print(f'Разделить = {calc.split()}')
print(f'Умножить = {calc.multiply()}')
print(f'Степень = {calc.my_pow()}')
print(f'Квадрат = {calc.squared(0)}')
print(f'Квадрат = {calc.squared(1)}')
