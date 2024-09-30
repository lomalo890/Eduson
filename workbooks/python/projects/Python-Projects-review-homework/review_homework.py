from abc import ABC, abstractmethod

class Shape(ABC):

    def __init__(self):
        pass
    @abstractmethod
    def get_area(self):
        pass
    @abstractmethod
    def get_length(self):
        pass


class RightTriagle(Shape):

    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_area(self):
        return (self.side_a * self.side_b) / 2


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def get_length(self):
        return 2 * 3.14 * self.radius

