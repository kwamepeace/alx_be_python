import math
class Shape:
    def __init__(self):
        pass
        

    def area(self):
        raise NotImplementedError("Subclasses must implement this method")
    

class Rectangle(Shape):
    def __init__(self, width, length):
        super().__init__()
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length
    

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
