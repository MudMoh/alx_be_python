import math

class Shape:
    """
    A base class for geometric shapes.
    """
    def area(self):
        """
        Calculates the area of the shape. This method should be overridden by subclasses.
        """
        raise NotImplementedError("Subclasses should implement this method.")

class Rectangle(Shape):
    """
    A class for a rectangle, inheriting from Shape.
    """
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """
        Calculates the area of the rectangle.
        """
        return self.length * self.width

class Circle(Shape):
    """
    A class for a circle, inheriting from Shape.
    """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """
        Calculates the area of the circle.
        """
        return math.pi * (self.radius ** 2)
