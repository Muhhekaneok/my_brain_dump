import unittest
from src.two_sum_problem import get_two_sum_indices

class TestTwoSumProblem(unittest.TestCase):
    def test_the_problem(self):
        self.assertEqual(get_two_sum_indices([2, 8, 7, 3], 9), (0, 2))
        self.assertEqual(get_two_sum_indices([5, 1, 4, 9, 3], 10), (1, 3))
        self.assertEqual(get_two_sum_indices([2, 8, 7, 3, 0, 1], 3), (3, 4))

    def test_negative_elements(self):
        self.assertEqual(get_two_sum_indices([-8, 0, -5, -11, -1, -7], -6), (2, 4))

    def test_empty_list(self):
        self.assertEqual(get_two_sum_indices([], 1), ())
        self.assertEqual(get_two_sum_indices([], 3), ())
        self.assertEqual(get_two_sum_indices([], 99), ())

    def test_no_match(self):
        self.assertEqual(get_two_sum_indices([1, 2, 3], 101), ())

    def test_type_error(self):
        with self.assertRaises(TypeError):
            get_two_sum_indices(["1", "2", "3"], 1)
        with self.assertRaises(TypeError):
            get_two_sum_indices([1, 2, 3], "5")
        with self.assertRaises(TypeError):
            get_two_sum_indices([1, "2", 3.5], 5)
        with self.assertRaises(TypeError):
            get_two_sum_indices(1, 1)