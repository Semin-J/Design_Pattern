from enum import Enum
from math import *


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'x: {self.x}, y: {self.y}'
    # def __init__(self, a, b, system=CoordinateSystem.CARTESIAN):
    #     if system == CoordinateSystem.CARTESIAN:
    #         self.x = a
    #         self.y = b
    #     elif system == CoordinateSystem.POLAR:
    #         self.x = a * cos(b)
    #         self.y = a * sin(b)

    # Factory method is alternative of complicated initializer
    # If there are too many static method, we can make another entity
    
    # Making it as inner class, and get rid of @staticmethod
    class PointFactory:
        # add self, as became inner class
        def new_cartesian_point(self, x, y):
            return Point(x, y)

        def new_polar_point(self, rho, theta):
            return Point(rho * cos(theta), rho * sin(theta))
    
    # let PointFactory act as a static fashion
    # Singelton...?!
    factory = PointFactory()


if __name__ == "__main__":
    p = Point(2, 3)
    # p2 = Point.PointFactory.new_polar_point(1, 2)
    p2 = Point.factory.new_polar_point(1, 2)
    print(p, p2)