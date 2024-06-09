"""
Problem:

Obtain the string that arranges letters of the string “stressed” in reverse order (tail to head).
"""
import unittest
from parameterized import parameterized_class
from src.p0 import reverse_string


@parameterized_class(('test_string', 'expected_output'), [
    ("stressed", "desserts"),
    ("random", "modnar"),
    ("konnichiwa", "awihcinnok"),
    ("AppA", "AppA")
])
class TestP0Chapter1(unittest.TestCase):
    def test_should_reverse_string(self):
        self.assertEqual(
            reverse_string(
                self.test_string),
            self.expected_output)


if __name__ == "__main__":
    unittest.main()
