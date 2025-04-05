import unittest
from src.string_reversal import get_reverse_loop

class GetStringReverseLoop(unittest.TestCase):
    def test_common_strings(self):
        self.assertEqual(get_reverse_loop("Python"), "nohtyP")
        self.assertEqual(get_reverse_loop("hello"), "olleh")
        self.assertEqual(get_reverse_loop("mama"), "amam")
        self.assertEqual(get_reverse_loop("madam"), "madam")

    def test_with_spaces(self):
        self.assertEqual(get_reverse_loop("mama mia"), "aim amam")
        self.assertEqual(get_reverse_loop(" "), " ")

    def test_empty_strings(self):
        self.assertEqual(get_reverse_loop(""), "")

    def test_type_error(self):
        with self.assertRaises(TypeError):
            get_reverse_loop(123)
        with self.assertRaises(TypeError):
            get_reverse_loop([1, 2, 3])
        with self.assertRaises(TypeError):
            get_reverse_loop((1, 2, 3))
        with self.assertRaises(TypeError):
            get_reverse_loop({"one": 1})
        with self.assertRaises(TypeError):
            get_reverse_loop(None)
        with self.assertRaises(TypeError):
            get_reverse_loop(True)