import unittest
from circle import circle

class CircleTestCase(unittest.TestCase):
    def test_normal_radius(self):
        result = circle(10)
        self.assertEqual(result, 314)

    def test_zero_radius(self):
        result = circle(0)
        self.assertEqual(result, 0)

    def test_under_zero_radius(self):
        result = circle(-5)
        self.assertEqual(result, 0)