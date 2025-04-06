import unittest
from src.string_reversal import get_reverse_loop, get_reverse_slice


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


class GetStringReverseSlice(unittest.TestCase):
    def test_common_strings(self):
        self.assertEqual(get_reverse_slice("bred"), "derb")
        self.assertEqual(get_reverse_slice("Python"), "nohtyP")
        self.assertEqual(get_reverse_loop("laptop"), "potpal")
        self.assertEqual(get_reverse_loop("racecar"), "racecar")
        self.assertEqual(get_reverse_loop("-12345"), "54321-")

    def test_with_space(self):
        self.assertEqual(get_reverse_loop("game over"), "revo emag")
        self.assertEqual(get_reverse_loop(" "), " ")

    def test_empty_space(self):
        self.assertEqual(get_reverse_loop(""), "")

    def test_type_error(self):
        with self.assertRaises(TypeError):
            get_reverse_loop(9)
        with self.assertRaises(TypeError):
            get_reverse_slice([1, 2, 3])
