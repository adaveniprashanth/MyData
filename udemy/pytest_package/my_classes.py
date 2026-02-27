import math
from abc import ABC,abstractmethod
class Shape(ABC):
    def __init__(self,name):
        self.name=name

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius=radius

    def area(self):
        return math.pi* self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, name, length,width):
        super().__init__(name)
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width

    def perimeter(self):
        return 2*(self.length+self.width)

class Square(Rectangle):
    def __init__(self,side):
        super().__init__("square",side,side)
        self.side=side

    def perimeter(self):
        return 4*self.side

    def area(self):
        return self.side**2

# c=Circle("circle",20)
# print(c.name)
# print(c.area())

# r=Rectangle("rectangle",10,20)
# print(r.name)
# print(r.area())