"""
Problem:

Let the sets of letter bi-grams from the words “paraparaparadise” and “paragraph” $X$ and $Y$, respectively.
Obtain the union, intersection, difference of the two sets. In addition, check whether the bigram “se” is included in the sets $X$ and $Y$
"""
import unittest
from parameterized import parameterized
from src.p6 import get_union_bigram, get_intersection_bigram, get_difference_bigram, check_word_in_bigrams


class TestP6Chapter1(unittest.TestCase):

    @parameterized.expand([
        (
            "paraparaparadise",
            "paragraph",
            {'ar', 'ad', 'is', 'ph', 'pa', 'di', 'se', 'gr', 'ap', 'ra', 'ag'}
        ),
        (
            "papaklopaklo",
            "bapaklopakpak",
            {'ak', 'pa', 'lo', 'kl', 'ap', 'op', 'ba', 'kp'}
        )
    ])
    def test_should_get_bigram_union(
            self, string1: str, string2: str, expected_output: list[str]):
        self.assertEqual(get_union_bigram(string1, string2), expected_output)

    @parameterized.expand([
        (
            "paraparaparadise",
            "paragraph",
            {'ar', 'pa', 'ra', 'ap'}
        ),
        (
            "papaklopaklo",
            "bapaklopakpak",
            {'ak', 'pa', 'lo', 'kl', 'ap', 'op'}
        )
    ])
    def test_should_get_bigram_intersection(
            self, string1: str, string2: str, expected_output: list[str]):
        self.assertEqual(
            get_intersection_bigram(
                string1,
                string2),
            expected_output)

    @parameterized.expand([
        (
            "paraparaparadise",
            "paragraph",
            {'ad', 'is', 'di', 'se'}
        ),
        (
            "papaklopaklo",
            "bapaklopakpak",
            set()
        )
    ])
    def test_should_get_bigram_difference(
            self, string1: str, string2: str, expected_output: list[str]):
        self.assertEqual(
            get_difference_bigram(
                string1,
                string2),
            expected_output)

    @parameterized.expand([
        (
            "paraparaparadise",
            "paragraph",
            "se",
            False
        ),
        (
            "papaklopaklo",
            "bapaklopakpak",
            "lo",
            True
        )
    ])
    def test_should_check_word_in_bigram(
            self, string1: str, string2: str, bigram_to_check: str, expected_output: bool):
        self.assertEqual(check_word_in_bigrams(
            [string1, string2], bigram_to_check), expected_output)


if __name__ == "__main__":
    unittest.main()
