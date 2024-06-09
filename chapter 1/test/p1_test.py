"""
Problem:

Obtain the string that concatenates the 1st, 3rd, 5th, and 7th letters in the string “schooled”.
"""

import unittest

from parameterized import parameterized_class
from src.p1 import join_chars_in_string


@parameterized_class(('test_string', 'chars_in_string', 'expected_output'), [
    ("schooled", [1, 3, 5, 7], "shoe"),
    ("congratulations", [1, 8, 9, 10, 15], "culas")
])
class TestP1Chapter1(unittest.TestCase):

    def test_should_join_character(self):
        chars_in_string = [i - 1 for i in self.chars_in_string]
        self.assertEqual(
            join_chars_in_string(
                self.test_string,
                chars_in_string),
            self.expected_output)


if __name__ == "__main__":
    unittest.main()
