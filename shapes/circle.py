"""
Programming for linguists

Implementation of the class Circle
"""

import math

from shapes.shape import Shape


class Circle(Shape):
    """
    A class for circles
    """
    def __init__(self, uid: int, radius: int):
        super().__init__(uid)
        self.radius = radius

    def get_area(self):
        """
        Returns the area of a circle
        :return int: the area of a circle
        """
        return (self.radius ** 2) * math.pi

    def get_perimeter(self):
        """
        Returns the perimeter of a circle
        :return int: the perimeter of a circle
        """
        return self.get_diameter() * math.pi

    def get_diameter(self):
        """
        Returns the diameter of a circle
        :return int: the diameter of a circle
        """
        return self.radius * 2
