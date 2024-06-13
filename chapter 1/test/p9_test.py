"""
Problem:


Write a program with the specification:

Receive a word sequence separated by space
For each word in the sequence:
    If the word is no longer than four letters, keep the word unchanged
    Otherwise,
        Keep the first and last letters unchanged
        Shuffle other letters in other positions (in the middle of the word)
Observe the result by giving a sentence, e.g.,
“I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind “.
"""


import unittest
from parameterized import parameterized_class
from src.p9 import mix_middle_character


@parameterized_class(('input_string'), [
    ("I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind "),
    ("It is interesting to see that Artificial Intelligence can actually improve our life and productivity")

])
class TestP9Chapter1(unittest.TestCase):
    def test_should_mix_middle_character(self):
        mixed_string = mix_middle_character(self.input_string)
        self.assertTrue(check_mixed_string(self.input_string, mixed_string))


def check_mixed_string(original_string: str, mixed_string: str) -> bool:
    original_string_splitted = original_string.split()
    mixed_string_splitted = mixed_string.split()

    for i in range(len(original_string_splitted)):
        if len(original_string_splitted[i]) > 4:

            if check_palindrome(original_string[i]) and \
                (original_string_splitted[i] == mixed_string_splitted[i] or
                    original_string_splitted[i][0] != mixed_string_splitted[i][0] or
                    original_string_splitted[i][-1] != mixed_string_splitted[i][-1]):
                return False
    return True


def check_palindrome(string: str) -> bool:
    for i in range(len(string)):
        if string[i] != string[len(string) - 1 - i]:
            return False
    return True


if __name__ == "__main__":
    unittest.main()
