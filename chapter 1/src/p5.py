"""
Problem:

Implement a function that obtains n-grams from a given sequence object (e.g., string and list).
Use this function to obtain word bi-grams and letter bi-grams from the sentence “I am an NLPer”
"""


def genereate_word_ngram(n: int, string: str) -> list[tuple[str]]:
    list_word = string.split()
    word_pair = []
    word_ngram = []
    for i in range(len(list_word) - (n - 1)):
        for j in range(n):
            word_pair.append(list_word[i + j])
        word_ngram.append(tuple(word_pair))
        word_pair = []
    return word_ngram


def generate_letter_ngram(n: int, string) -> list[str]:
    char_list = [None] * len(string)
    char_list_pointer = 0

    for i in range(len(string)):
        # If character is an alphabet
        if (ord(string[i]) >= 65 and ord(string[i]) <= 90) or (
                ord(string[i]) >= 97 and ord(string[i]) <= 122):
            char_list[char_list_pointer] = string[i]
            char_list_pointer += 1

    letter_pair = []
    letter_ngram = []
    for i in range(char_list_pointer - (n - 1)):
        for j in range(n):
            letter_pair.append(char_list[i + j])
        letter_ngram.append("".join(letter_pair))
        letter_pair = []
    return letter_ngram
