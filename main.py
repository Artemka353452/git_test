from math import pi


class Circle:
    def __init__(self, r):
        self._r = r

    def area(self):
        return pi * (self._r ** 2)

    def set_height(self, a):
        self._a = a

    def set_width(self, b):
        self._b = b


<<<<<<< HEAD
main_rect = Rectangle(5, 4)
print(main_rect.area())
main_rect.set_height(7)
main_rect.set_width(8)
=======
main_circle = Circle(2)
print(main_circle.area())
>>>>>>> new_class
