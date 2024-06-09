"""
Problem:

Obtain the string “schooled” by concatenating the letters in “shoe” and “cold” one after the other from head to tail.
"""


def join_string_interchangeably(string1: str, string2: str) -> str:
    string_length1 = len(string1)
    string_length2 = len(string2)
    joined_string_length = string_length1 + string_length2
    joined_string = [None] * joined_string_length
    idx_string1 = 0
    idx_string2 = 0
    for i in range(joined_string_length):
        if idx_string1 < string_length1 and idx_string2 < string_length2:
            if i % 2 == 0:
                joined_string[i] = string1[idx_string1]
                idx_string1 += 1
            if i % 2 == 1:
                joined_string[i] = string2[idx_string2]
                idx_string2 += 1

        elif idx_string1 < string_length1:
            joined_string[i] = string1[idx_string1]
            idx_string1 += 1
        elif idx_string2 < string_length2:
            joined_string[i] = string2[idx_string2]
            idx_string2 += 1

    return "".join(joined_string)
