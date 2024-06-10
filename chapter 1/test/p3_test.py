"""
Problem:

Split the sentence “Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics”. 
into words, and create a list whose element presents the number of alphabetical letters in the corresponding word.
"""

import unittest
from parameterized import parameterized_class
from src.p3 import split_word_count_char

STRING_INPUT1="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics"
STRING_INPUT2="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation"


@parameterized_class(('string', 'expected_output'), [
    (STRING_INPUT1, [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]),
    (STRING_INPUT2, [5, 5, 5, 3, 4, 11, 10, 4, 3, 2, 7, 6, 10, 2, 6, 2, 6, 5, 6, 2, 4, 2, 5, 6, 4, 7, 12])
])
class TestP3Chapter1(unittest.TestCase):
    def test_should_count_char_in_word(self):
        self.assertEqual(split_word_count_char(self.string),self.expected_output)

if __name__ == "__main__":
    unittest.main()