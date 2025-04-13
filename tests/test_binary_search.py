import unittest
from src.binary_search import get_binary_search


class TestGetBinarySearch(unittest.TestCase):
    def test_found(self):
        self.assertNotEqual(get_binary_search([1, 3, 5, 7, 9], 5), -1)
        self.assertNotEqual(get_binary_search([10, 20, 30, 40, 50], 10), -1)

    def test_not_found(self):
        self.assertEqual(get_binary_search([1, 3, 5, 7, 9], 8), -1)
        self.assertEqual(get_binary_search([], 5), -1)

    def test_unsorted_list(self):
        self.assertNotEqual(get_binary_search([2, 9, 3, -4, 8], 9), -1)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            get_binary_search("12345", 5)
        with self.assertRaises(TypeError):
            get_binary_search([4, 0, -1, 9, 5], "3")
