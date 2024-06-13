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


def mix_middle_character(string: str) -> str:
    string_splitted = string.split()
    print(string_splitted)
    for i in range(len(string_splitted)):
        word_char_list = list(string_splitted[i])
        word_char_list_length = len(word_char_list)
        # Reverse the middle string
        if word_char_list_length > 4:
            for j in range(1, word_char_list_length // 2):
                word_char_list[j], word_char_list[word_char_list_length - 1 - j] = \
                    word_char_list[word_char_list_length -
                                   1 - j], word_char_list[j]
            mixed_word_chars = "".join(word_char_list)
            string_splitted[i] = mixed_word_chars

    return " ".join(string_splitted)
