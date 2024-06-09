"""
Problem:

Obtain the string that arranges letters of the string “stressed” in reverse order (tail to head).
"""


def reverse_string(string: str) -> str:
    string_length = len(string)
    string_list = list(string)
    for i in range(string_length // 2):
        string_list[i], string_list[string_length - 1 -
                                    i] = string_list[string_length - 1 - i], string_list[i]
    return "".join(string_list)
