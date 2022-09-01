# A component responsible solely for the wholesale 
# (not piecewise) creation of objects
from math import *

class Point:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y  = y


    def __str__(self) -> str:
        return f'x: {self.x}, y:{self.y}'


class PointFactory:
    @staticmethod
    def new_cartesian_point(x,y):
        return Point(x,y)
    
    @staticmethod
    def new_polar_point(rho,theta):
        return Point(rho*cos(theta),rho*sin(theta))

if __name__ == '__main__':
    p = Point(2,3)
    p2 = PointFactory.new_polar_point(1,2)
    print(p,p2)
    