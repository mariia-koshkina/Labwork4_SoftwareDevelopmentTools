import unittest
from triangle import triangle

class TriangleTestCase(unittest.TestCase):
    def test_normal_values(self):
        result = triangle(10, 5)
        self.assertEqual(result, 25)

    def test_zero_value(self):
        result = triangle(0, 10)
        self.assertEqual(result, 0)

    def test_under_zero_value(self):
        result = triangle(-10, 5)
        self.assertEqual(result, 0)

    def test_float_values(self):
        result = triangle(2.5, 4)
        self.assertEqual(result, 5)