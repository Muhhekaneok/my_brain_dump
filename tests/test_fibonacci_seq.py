import unittest
from src.fibonacci_sequence import get_fibonacci_seq

class GetFibonacciSequence(unittest.TestCase):
    def test_base_cases(self):
        self.assertEqual(get_fibonacci_seq(0), [])
        self.assertEqual(get_fibonacci_seq(1), [0])
        self.assertEqual(get_fibonacci_seq(2), [0, 1])

    def test_fibonacci(self):
        self.assertEqual(get_fibonacci_seq(5), [0, 1, 1, 2, 3])
        self.assertEqual(get_fibonacci_seq(7), [0, 1, 1, 2, 3, 5, 8])
        self.assertEqual(get_fibonacci_seq(9), [0, 1, 1, 2, 3, 5, 8, 13, 21])

    def test_type_error(self):
        with self.assertRaises(TypeError):
            get_fibonacci_seq("4")
        with self.assertRaises(TypeError):
            get_fibonacci_seq(5.3)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            get_fibonacci_seq(-1)