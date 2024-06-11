"""
Problem:

Split the sentence “Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can”.
into words, and extract the first letter from the 1st, 5th, 6th, 7th, 8th, 9th, 15th, 16th, 19th words and the first two letters from the other words.
Create an associative array (dictionary object or mapping object) that maps from the extracted string to the position (offset in the sentence) of the corresponding word.
"""
from typing import Dict


def create_atom_from_sentence(
        string: str, selected_word_idx: list[int]) -> Dict[str, int]:
    word_count = 0
    word_counter = set()
    set_word_idx = set(selected_word_idx)
    result = {}
    key = ""
    value = ""
    for i in range(len(string)):
        # If character is an alphabet
        if (ord(string[i]) >= 65 and ord(string[i]) <= 90) or (
                ord(string[i]) >= 97 and ord(string[i]) <= 122):
            # Start count for the first time
            if word_count == 0:
                word_count = 1

            # For every word in the sentence we get the first one or two
            # characters and save it to the dictionary
            if word_count not in word_counter:
                if word_count in set_word_idx:
                    key = string[i]
                    value = word_count
                    if key not in result:
                        result[key] = value
                else:
                    key = string[i] + string[i + 1]
                    value = word_count
                    if key not in result:
                        result[key] = value
                word_counter.add(word_count)

        # If character is white space
        elif ord(string[i]) == 32:
            word_count += 1

    return result
