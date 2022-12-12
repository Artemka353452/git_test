from math import pi


class Rectangle:
    def __init__(self, a, b):
        self._a = a
        self._b = b

    def area(self):
        return self._a * self._b

    def get_height(self):
        return self._a

    def get_width(self):
        return self._b

    def set_height(self, a):
        self._a = a

    def set_width(self, b):
        self._b = b


class Circle:
    def __init__(self, r):
        self._r = r

    def area(self, r):
        return pi * self._r ** 2


main_rect = Rectangle(5, 4)
print(main_rect.area())
main_rect.set_height(7)
main_rect.set_width(8)
main_circle = Circle(2)
print(main_circle.area(12))
