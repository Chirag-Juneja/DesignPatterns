# A mechanism that decouples an interface (hierarchy)
# from implementation (hierarchy)
from abc import ABC, abstractmethod
from turtle import color

class Color(ABC):
    @abstractmethod
    def fill(self):
        pass

class Red(Color):
    def fill(self):
        return 'Color is Red'

class Blue(Color):
    def fill(self):
        return 'Color is Blue'


class Shape(ABC):
    def __init__(self,color) -> None:
        self.color= color

class Circle(Shape):
    def __init__(self, color) -> None:
        super().__init__(color)
    
    def draw(self):
        print("Circle: "+ self.color.fill())

class Rectangle(Shape):
    def __init__(self, color) -> None:
        super().__init__(color)
    
    def draw(self):
        print("Rectangle: "+ self.color.fill())
    
if __name__ == '__main__':
    blue = Blue()
    red = Red()
    circle = Circle(blue)
    rectangle = Rectangle(red)
    circle.draw()
    rectangle.draw()
