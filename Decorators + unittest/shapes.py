from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @property
    @abstractmethod
    def area(self):
        pass

    @property
    @abstractmethod
    def perimeter(self):
        pass

    @classmethod
    @abstractmethod
    def from_string(cls, data: str):
        pass

#КРУГ
class Circle(Shape):
    def __init__(self, radius: float):
        self.validate_radius(radius)
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, new_value):
        self.validate_radius(new_value)
        self.__radius = new_value

    @property
    def area(self):
        return math.pi * pow(self.__radius,2)

    @property
    def perimeter(self):
        return 2 * math.pi * self.__radius

    @classmethod
    def from_string(cls, data: str):
        circle, value = data.split(",")
        return cls(float(value))

    @staticmethod
    def validate_radius(value: float):
        if value < 0:
            raise ValueError
        return True

#ПРЯМОУГОЛЬНИК
class Rectangle(Shape):
    def __init__(self, width, height):
        self.validate_sides(width, height)
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, new_width):
        self.validate_sides(new_width, self.__height)
        self.__width = new_width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_height):
        self.validate_sides(self.__width, new_height)
        self.__height = new_height

    @property
    def area(self):
        return self.__width * self.__height

    @property
    def perimeter(self):
        return (self.__width + self.__height) * 2

    @classmethod
    def from_string(cls, data: str):
        rect, value1, value2 = data.split(",")
        return cls(float(value1), float(value2))

    @staticmethod
    def validate_sides(width: float, height: float):
        if width < 0 or height < 0:
            raise ValueError
        return True

#КВАДРАТ
class Square(Rectangle):
    def __init__(self, side: float):
        super().__init__(side, side)

    @classmethod
    def from_string(cls, data: str):
        square, value = data.split(",")
        return cls(float(value))


