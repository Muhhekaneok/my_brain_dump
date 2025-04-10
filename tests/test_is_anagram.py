import unittest
from src.anagram_checker import is_anagram_2_dicts

class TestIsAnagramTwoDicts(unittest.TestCase):
    def test_anagram(self):
        self.assertEqual(is_anagram_2_dicts("silent", "listen"), True)
        self.assertEqual(is_anagram_2_dicts("cheater", "teacher"), True)
        self.assertEqual(is_anagram_2_dicts("a gentleman", "elegant man"), True)
        self.assertEqual(is_anagram_2_dicts("forty five", "over fifty"), True)
        self.assertEqual(is_anagram_2_dicts("coronavirus", "carnivorous"), True)

    def test_emtpy_lines(self):
        self.assertEqual(is_anagram_2_dicts("", ""), True)

    def test_not_anagram(self):
        self.assertEqual(is_anagram_2_dicts("new york times", "monkeys write"), False)
        self.assertEqual(is_anagram_2_dicts("funeral", "real fun"), False)
        self.assertEqual(is_anagram_2_dicts(" ", ""), False)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            is_anagram_2_dicts(1, "a")
        with self.assertRaises(TypeError):
            is_anagram_2_dicts([], "b")
        with self.assertRaises(TypeError):
            is_anagram_2_dicts([], ())