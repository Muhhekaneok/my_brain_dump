import unittest
from src.prime_number_checker import is_prime_number


class TestPrimeNumberChecker(unittest.TestCase):
    def test_is_prime(self):
        self.assertEqual(is_prime_number(2), True)
        self.assertEqual(is_prime_number(3), True)
        self.assertEqual(is_prime_number(5), True)
        self.assertEqual(is_prime_number(7), True)
        self.assertEqual(is_prime_number(11), True)
        self.assertEqual(is_prime_number(13), True)
        self.assertEqual(is_prime_number(997), True)

    def test_is_not_prime(self):
        self.assertEqual(is_prime_number(4), False)
        self.assertEqual(is_prime_number(6), False)
        self.assertEqual(is_prime_number(9), False)
        self.assertEqual(is_prime_number(15), False)
        self.assertEqual(is_prime_number(999), False)

    def test_negative_value(self):
        with self.assertRaises(ValueError):
            is_prime_number(-4)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            is_prime_number("a")
        with self.assertRaises(TypeError):
            is_prime_number([10])
