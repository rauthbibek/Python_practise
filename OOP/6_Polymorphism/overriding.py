from math import pi
class Shape:

    def __init__(self,name):
        self.name = name

    def area(self):
        pass

    def __str__(self):
        return self.name

    def fact(self):
        print("It's two dimensional shape")

class Square(Shape):

    def __init__(self,length):
        super().__init__("Square")
        self.length = length

    def area(self):
        return self.length**2

    def fact(self):
        print("It's a Square")

class Circle(Shape):

    def __init__(self,radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return pi*self.radius**2

square = Square(10)
circle = Circle(4)
print(f"Area of {square.__str__()} is {square.area()}")
square.fact()
print(f"Area of {circle.__str__()} is {circle.area()}")
circle.fact()