import unittest
from src.factorial_calculator import get_factorial_recursive, get_factorial_iterative


class TestGetFactorialRecursive(unittest.TestCase):
    def test_base_cases(self):
        self.assertEqual(get_factorial_recursive(0), 1)
        self.assertEqual(get_factorial_recursive(1), 1)

    def test_recursive_cases(self):
        self.assertEqual(get_factorial_recursive(3), 6)
        self.assertEqual(get_factorial_recursive(5), 120)
        self.assertEqual(get_factorial_recursive(7), 5040)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            get_factorial_recursive("5")
        with self.assertRaises(TypeError):
            get_factorial_recursive(3.4)

    def test_negative_value(self):
        with self.assertRaises(ValueError):
            get_factorial_recursive(-7)


class TestGetFactorialIterative(unittest.TestCase):
    def test_base_cases(self):
        self.assertEqual(get_factorial_iterative(0), 1)
        self.assertEqual(get_factorial_iterative(1), 1)

    def test_iterative_cases(self):
        self.assertEqual(get_factorial_iterative(3), 6)
        self.assertEqual(get_factorial_iterative(5), 120)
        self.assertEqual(get_factorial_iterative(7), 5040)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            get_factorial_iterative("1")
        with self.assertRaises(TypeError):
            get_factorial_iterative(7.8)

    def test_negative_value(self):
        with self.assertRaises(ValueError):
            get_factorial_iterative(-1)
