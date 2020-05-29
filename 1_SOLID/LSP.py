# LSP (Liskov Substitution Principle)
# Derived class instance should be able to substitued with Base class(interface) instance
# with no modification of attributes and methods of derived class

class Rectangle:
    def __init__(self, width, height):
        # _var: convention, treat it as a private / need more explanation
        self._width = width
        self._height = height

    @property
    def area(self):
        return self._height * self._width

    def __str__(self):
        return f'Width: {self.width}, Height: {self.height}'
    
    @property  # getter
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property  # getter
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value


# Many solution to fix it
# One thing is no need Square class
# but add attribute to check the width and height in Rectangle class

# This class violate Liskov Substitution Principle
class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)
    
    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value


def use_it(rec):
    w = rec.width
    rec.height = 10
    expected = w * 10
    print(f'Expected area is {expected}, got {rec.area}')

if __name__ == "__main__":
    
    rec = Rectangle(2, 3)
    use_it(rec)  # Expected area is 20, got 20

    sqr = Square(3)
    use_it(sqr)  # Expected area is 30, got 100