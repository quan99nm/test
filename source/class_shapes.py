import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

"create rectangle class"
class rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    "add equal method for rectangle"
    def __eq__(self, other):
        return self.length == other.length and self.width == other.width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)