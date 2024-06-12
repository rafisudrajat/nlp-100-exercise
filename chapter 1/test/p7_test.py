"""
Problem:

Implement a function that receives arguments, x, y, and z and returns a string “{y} is {z} at {x}”, where “{x}”, “{y}”, and “{z}” denote the values of x, y, and z, respectively.
In addition, confirm the return string by giving the arguments x=12, y="temperature", and z=22.4.
"""

import unittest
from parameterized import parameterized
from src.p7 import concatenate_string


class TestP7Chapter1(unittest.TestCase):
    @parameterized.expand([
        (12, "temperature", 22.4, "temperature is 22.4 at 12"),
        ("Bandung", "Air", "Wet", "Air is Wet at Bandung")
    ])
    def test_should_concatenate_string(self, x, y, z, expected_output: str):
        self.assertEqual(
            concatenate_string(
                x,
                y,
                z,
                r"{y} is {z} at {x}"),
            expected_output)


if __name__ == "__main__":
    unittest.main()
