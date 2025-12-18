import unittest
from square import square

class SquareTestCase(unittest.TestCase):
    def test_normal_side(self):
        result = square(4)
        self.assertEqual(result, 16)

    def test_zero_side(self):
        result = square(0)
        self.assertEqual(result, 0)

    def test_under_zero_side(self):
        result = square(-6)
        self.assertEqual(result, 0)