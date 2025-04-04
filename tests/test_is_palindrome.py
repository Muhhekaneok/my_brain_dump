import unittest
from src.palindrome_checker import is_palindrome

class TestIsPalindrome(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("noon"))

    def test_not_is_palindrome(self):
        self.assertFalse(is_palindrome("python"))
        self.assertFalse(is_palindrome("brain"))

    def test_is_empty(self):
        self.assertTrue(is_palindrome(""))

    def test_single_chart(self):
        self.assertTrue(is_palindrome("a"))

    def test_type_error(self):
        with self.assertRaises(TypeError):
            is_palindrome(12321)