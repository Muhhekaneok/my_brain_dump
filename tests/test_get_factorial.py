import unittest
from src.factorial_calculator import get_factorial

class TestGetFactorial(unittest.TestCase):
    def test_base_cases(self):
        self.assertEqual(get_factorial(0), 1)
        self.assertEqual(get_factorial(1), 1)

    def test_recursive_cases(self):
        self.assertEqual(get_factorial(3), 6)
        self.assertEqual(get_factorial(5), 120)
        self.assertEqual(get_factorial(7), 5040)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            get_factorial("5")
        with self.assertRaises(TypeError):
            get_factorial(3.4)

    def test_negative_value(self):
        with self.assertRaises(ValueError):
            get_factorial(-7)