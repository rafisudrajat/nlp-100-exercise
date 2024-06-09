"""
Problem:

Obtain the string “schooled” by concatenating the letters in “shoe” and “cold” one after the other from head to tail.
"""
import unittest
from parameterized import parameterized_class
from src.p2 import join_string_interchangeably


@parameterized_class(('string1', 'string2', 'expected_output'), [
    ("shoe", "cold", "schooled"),
    ("iOS", "Android", "iAOnSdroid"),
    ("Japan", "Indo", "JIanpdaon"),
    ("Freedom", "Air", "FArieredom"),

])
class TestP2Chapter1(unittest.TestCase):
    def test_should_join_character_interchangeably(self):
        self.assertEqual(
            join_string_interchangeably(
                self.string1,
                self.string2),
            self.expected_output)


if __name__ == "__main__":
    unittest.main()
