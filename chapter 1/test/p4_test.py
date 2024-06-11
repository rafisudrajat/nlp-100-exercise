"""
Problem:

Split the sentence “Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can”.
into words, and extract the first letter from the 1st, 5th, 6th, 7th, 8th, 9th, 15th, 16th, 19th words and the first two letters from the other words.
Create an associative array (dictionary object or mapping object) that maps from the extracted string to the position (offset in the sentence) of the corresponding word.
"""

import unittest
from parameterized import parameterized_class
from src.p4 import create_atom_from_sentence

STRING_INPUT1 = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can"
EXPECTED_OUTPUT1 = {
    "H": 1,
    "He": 2,
    "Li": 3,
    "Be": 4,
    "B": 5,
    "C": 6,
    "N": 7,
    "O": 8,
    "F": 9,
    "Ne": 10,
    "Na": 11,
    "Mi": 12,
    "Al": 13,
    "Si": 14,
    "P": 15,
    "S": 16,
    "Cl": 17,
    "Ar": 18,
    "K": 19,
    "Ca": 20}


@parameterized_class(('string', 'selected_word_idx', 'expected_output'), [
    (STRING_INPUT1, [1, 5, 6, 7, 8, 9, 15, 16, 19], EXPECTED_OUTPUT1)
])
class TestP4Chapter1(unittest.TestCase):
    def test_should_create_dummy_atom_name(self):
        self.assertEqual(
            create_atom_from_sentence(
                self.string,
                self.selected_word_idx),
            self.expected_output)


if __name__ == "__main__":
    unittest.main()
