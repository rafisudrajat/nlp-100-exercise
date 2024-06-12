"""
Problem:

Implement a function cipher that converts a given string with the specification:

Every alphabetical lowercase letter c is converted to a letter whose ASCII code is (219 - [the ASCII code of c])
Keep other letters unchanged
"""


def chiper_message(message: str) -> str:
    list_char = [str(219 - 99) if c == 'c' else c for c in message]
    return "".join(list_char)
