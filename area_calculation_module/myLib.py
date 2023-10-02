from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self, *args):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("The circle radius value must be greater than zero.")
        self._radius = value

    def area(self):
        S = math.pi * self._radius ** 2
        return S


class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float) -> None:
        self.sides = sorted([a, b, c])

    @property
    def sides(self) -> list[float]:
        return self._sides

    @sides.setter
    def sides(self, value: list[float]) -> None:
        if not (value[0] > 0 and value[1] > 0 and value[2] > 0):
            raise ValueError("The sides of the triangle must be greater than zero.")
        if not (value[0] < value[1] + value[2] and value[1] < value[0] + value[2] and value[2] < value[0] + value[1]):
            raise ValueError("It is impossible to construct a triangle with such side values.")
        self._sides = sorted(value)

    def area(self):
        #Формула прямоугольного треугольника
        if self.is_right_triangle():
            S = self._sides[0] * self._sides[1] / 2
        else:
        #Формула Герона
            p = (self._sides[0] + self._sides[1] + self._sides[2]) / 2
            S = (p * (p - self._sides[0]) * (p - self._sides[1]) * (p - self._sides[2]))**(0.5)
        return S

    def is_right_triangle(self):
        if math.isclose(self._sides[2] ** 2, self._sides[0] ** 2 + self._sides[1] ** 2):
            return True
        else:
            return False

def calculate_area(*args):
    if len(args) == 1:
        shape = Circle(args[0])
    elif len(args) == 3:
        shape = Triangle(*args)
    else:
        raise ValueError("Unsupported shape. Only circle and triangle are supported.")
    return shape.area()

