"""
Problem:

Implement a function cipher that converts a given string with the specification:

Every alphabetical lowercase letter c is converted to a letter whose ASCII code is (219 - [the ASCII code of c])
Keep other letters unchanged
"""

import unittest
from parameterized import parameterized_class
from src.p8 import chiper_message


@parameterized_class(('message', 'expected_output'), [
    ("My name is Charlie, This is a random message in English",
     "My name is Charlie, This is a random message in English"),
    (
        "Can you come to the café on Cedar and Cherry? Cindy and Carl are celebrating their coding success. Casual dress, with coffee, cake, and cookies. See you!",
        "Can you 120ome to the 120afé on Cedar and Cherry? Cindy and Carl are 120elebrating their 120oding su120120ess. Casual dress, with 120offee, 120ake, and 120ookies. See you!"
    )
])
class TestP8Chapter1(unittest.TestCase):
    def test_should_chiper_message(self):
        self.assertEqual(chiper_message(self.message), self.expected_output)


if __name__ == "__main__":
    unittest.main()
