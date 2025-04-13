import unittest
from src.bubble_sort import get_bubble_sort


class TestBubbleSortFullAction(unittest.TestCase):
    def test_unsorted_mixed_numbers(self):
        self.assertEqual(
            get_bubble_sort([2, 6, 1, 0, 4, -1, 5, 3]), [-1, 0, 1, 2, 3, 4, 5, 6]
        )

    def test_already_sorted(self):
        self.assertEqual(get_bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_negative_numbers(self):
        self.assertEqual(get_bubble_sort([-7, -2, -3, -5, -1, -6, -4]), [-7, -6, -5, -4, -3, -2, -1])

    def test_empty_list(self):
        self.assertEqual(get_bubble_sort([]), [])

    def test_single_element(self):
        self.assertEqual(get_bubble_sort([7]), [7])

    def test_duplicates(self):
        self.assertEqual(get_bubble_sort([3, 3, 3]), [3, 3, 3])

    def test_incorrect_elements(self):
        with self.assertRaises(TypeError):
            get_bubble_sort([11, 12, "13"])

    def test_type_error(self):
        with self.assertRaises(TypeError):
            get_bubble_sort("3")
        with self.assertRaises(TypeError):
            get_bubble_sort(10)
