import unittest

from src.prime_number_checker import is_prime_number, is_prime_number_optimized


class TestPrimeNumberChecker(unittest.TestCase):
    def test_is_prime(self):
        self.assertTrue(is_prime_number(2))
        self.assertTrue(is_prime_number(3))
        self.assertTrue(is_prime_number(5))
        self.assertTrue(is_prime_number(7))
        self.assertTrue(is_prime_number(11))
        self.assertTrue(is_prime_number(13))
        self.assertTrue(is_prime_number(997))

    def test_is_not_prime(self):
        self.assertFalse(is_prime_number(4))
        self.assertFalse(is_prime_number(6))
        self.assertFalse(is_prime_number(9))
        self.assertFalse(is_prime_number(15))
        self.assertFalse(is_prime_number(999))

    def test_negative_value(self):
        with self.assertRaises(ValueError):
            is_prime_number(-4)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            is_prime_number("a")
        with self.assertRaises(TypeError):
            is_prime_number([10])


class TestPrimeNumberCheckerOptimized(unittest.TestCase):
    def test_is_prime(self):
        self.assertTrue(is_prime_number_optimized(2))
        self.assertTrue(is_prime_number_optimized(3))
        self.assertTrue(is_prime_number_optimized(5))
        self.assertTrue(is_prime_number_optimized(7))
        self.assertTrue(is_prime_number_optimized(11))
        self.assertTrue(is_prime_number_optimized(13))
        self.assertTrue(is_prime_number_optimized(997))

    def test_is_not_prime(self):
        self.assertFalse(is_prime_number_optimized(4))
        self.assertFalse(is_prime_number_optimized(6))
        self.assertFalse(is_prime_number_optimized(9))
        self.assertFalse(is_prime_number_optimized(15))
        self.assertFalse(is_prime_number_optimized(999))

    def test_negative_value(self):
        with self.assertRaises(ValueError):
            is_prime_number_optimized(-4)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            is_prime_number_optimized("a")
        with self.assertRaises(TypeError):
            is_prime_number_optimized([10])
