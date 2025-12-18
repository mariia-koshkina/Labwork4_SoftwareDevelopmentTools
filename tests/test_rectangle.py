import unittest
from rectangle import rectangle

class RectangleTestCase(unittest.TestCase):
    def test_normal_sides(self):
        result = rectangle(6, 5)
        self.assertEqual(result, 30)

    def test_zero_side(self):
        result = rectangle(0, 10)
        self.assertEqual(result, 0)

    def test_under_zero_side(self):
        result = rectangle(-3, 5)
        self.assertEqual(result, 0)