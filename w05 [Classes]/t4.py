
class Shape:
    def __init__(self, base, height):
        self.base = base
        self.height = height

        
class Rectangle(Shape):
    def area(self):
        return self.base * self.height


class Triangle(Shape):
    def area(self):
        return 0.5 * self.base * self.height
