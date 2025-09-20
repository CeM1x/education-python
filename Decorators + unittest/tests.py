import unittest
import math
from tkinter.font import names

from shapes import Circle, Rectangle, Square

class TestCircle(unittest.TestCase):
    def test_area_and_perimeter(self):
        c = Circle(10)
        self.assertAlmostEqual(c.area, math.pi * 100)
        self.assertAlmostEqual(c.perimeter, 2 * math.pi * 10)

    def test_setter_and_validation(self):
        c = Circle(5)
        c.radius = 7
        self.assertEqual(c.radius, 7)

        with self.assertRaises(ValueError):
            c.radius = -3

    def test_from_string(self):
        c = Circle.from_string("Circle,4")
        self.assertEqual(c.radius, 4)
        self.assertIsInstance(c, Circle)

    def test_validate_radius(self):
        self.assertTrue(Circle.validate_radius(5))

        with self.assertRaises(ValueError):
            Circle.validate_radius(-3)


class TestRectangle(unittest.TestCase):
    def test_area_and_perimeter(self):
        r = Rectangle(10, 12)
        self.assertAlmostEqual(r.area, 120)
        self.assertAlmostEqual(r.perimeter, 44)

    def test_setter_and_validation(self):
        r = Rectangle(5,8)
        r.width = 6
        r.height = 9
        self.assertEqual(r.width, 6)
        self.assertEqual(r.height, 9)

        with self.assertRaises(ValueError):
            Rectangle.validate_sides(-1,-1)

    def test_from_string(self):
        r = Rectangle.from_string("Rectangle,3,4")
        self.assertIsInstance(r, Rectangle)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)

    def test_validate_sides(self):
        self.assertTrue(Rectangle.validate_sides(10, 30))

        with self.assertRaises(ValueError):
            Rectangle.validate_sides(-1,-1)


class TestSquare(unittest.TestCase):
    def test_area_and_perimeter(self):
        s = Square(5)
        self.assertAlmostEqual(s.area, 25)
        self.assertAlmostEqual(s.perimeter, 20)

    def test_inheritance(self):
        s = Square(6)
        self.assertIsInstance(s, Rectangle)
        self.assertIsInstance(s, Square)

    def test_from_string(self):
        s = Square.from_string("Square,6")
        self.assertIsInstance(s, Square)
        self.assertAlmostEqual(s.width, 6)
        self.assertAlmostEqual(s.height, 6)

if __name__ == "__main__":
    unittest.main()