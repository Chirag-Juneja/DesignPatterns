# Liskov Substitution Principle
# (LSP) states that objects of a superclass should be replaceable with objects
# of its subclasses without breaking the application

# It it looks like a duck, quacks like a duck, but it needs batteries
# You probably have wrong abstraction


class Rectangle:
    def __init__(self,width,height) -> None:
        self._width = width
        self._height = height
    
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self,value):
        self._height = value

    @property
    def area(self):
        return self.width*self.height

class Square(Rectangle):
    def __init__(self, size) -> None:
        super().__init__(size, size)
    
    @Rectangle.height.setter
    def height(self,value):
        self._width = self._height = value
    

    @Rectangle.width.setter
    def width(self,value):
        self._width = self._height = value

# Does not work same with Square Object 
def increase_area(rc,percent):
    print(f'Original Area {rc.area}')
    rc.height = rc.height*(1+percent)
    print(f'Updated Area {rc.area}')

rc = Rectangle(5,5)
sq = Square(5)
increase_area(rc,0.5)
increase_area(sq,0.5)
