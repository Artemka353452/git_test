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


main_rect = Rectangle(5, 4)
print(main_rect.area())
main_rect.set_height(7)
main_rect.set_width(8)
