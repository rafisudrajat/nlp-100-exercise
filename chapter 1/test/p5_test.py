"""
Problem:

Implement a function that obtains n-grams from a given sequence object (e.g., string and list). 
Use this function to obtain word bi-grams and letter bi-grams from the sentence “I am an NLPer”
"""

import unittest
from parameterized import parameterized
from src.p5 import generate_letter_ngram, genereate_word_ngram


class TestP5Chapter1(unittest.TestCase):
    @parameterized.expand([
        ("I am an NLPer", [("I", "am"), ("am", "an"), ("an", "NLPer")]),
        ("I am a Stanford University Student majoring in mechatronics",[("I", "am"), ("am", "a"), ("a", "Stanford"), ("Stanford", "University"), ("University", "Student"), ("Student", "majoring"), ("majoring", "in"), ("in", "mechatronics")])
    ])
    def test_should_generate_word_bigram(self, string:str,expected_output:list[tuple[str]]):
        self.assertEqual(genereate_word_ngram(2,string),expected_output)
        
    
    @parameterized.expand([
        ("I am an NLPer", ['Ia', 'am', 'ma', 'an', 'nN', 'NL', 'LP', 'Pe', 'er']),
        ("I am an Engineering Student",["Ia", "am", "ma", "an", "nE", "En", "ng", "gi", "in", "ne", "ee", "er", "ri", "in", "ng", "gS", "St", "tu", "ud", "de", "en", "nt"])
    ])
    
    def test_should_generate_letter_bigram(self,string:str,expected_output:list[str]):
        self.assertEqual(generate_letter_ngram(2,string),expected_output)


if __name__ == "__main__":
    unittest.main()
