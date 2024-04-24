class Square:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def perimeter(self):
        return self.a * 2 + self.b * 2

    def area(self):
        return self.a * self.b


my_square = Square(2, 4)
print(my_square.area(), my_square.perimeter())
