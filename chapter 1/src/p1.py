"""
Problem:

Obtain the string that concatenates the 1st, 3rd, 5th, and 7th letters in the string “schooled”.
"""


def join_chars_in_string(string: str, char_idxs: list[int]) -> str:
    new_str_length = len(char_idxs)
    # Allocate new list
    chars_list = [None] * new_str_length
    for i in range(new_str_length):
        chars_list[i] = string[char_idxs[i]]
    return "".join(chars_list)
