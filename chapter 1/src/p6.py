"""
Problem:

Let the sets of letter bi-grams from the words “paraparaparadise” and “paragraph” $X$ and $Y$, respectively.
Obtain the union, intersection, difference of the two sets. In addition, check whether the bigram “se” is included in the sets $X$ and $Y$
"""
from .p5 import generate_letter_ngram


def get_union_bigram(string1: str, string2: str) -> set[str]:
    set_letter_bigram1 = set(generate_letter_ngram(2, string1))
    set_letter_bigram2 = set(generate_letter_ngram(2, string2))
    return set_letter_bigram1.union(set_letter_bigram2)


def get_intersection_bigram(string1: str, string2: str) -> set[str]:
    set_letter_bigram1 = set(generate_letter_ngram(2, string1))
    set_letter_bigram2 = set(generate_letter_ngram(2, string2))
    return set_letter_bigram1.intersection(set_letter_bigram2)


def get_difference_bigram(string1: str, string2: str) -> set[str]:
    set_letter_bigram1 = set(generate_letter_ngram(2, string1))
    set_letter_bigram2 = set(generate_letter_ngram(2, string2))
    return set_letter_bigram1.difference(set_letter_bigram2)


def check_word_in_bigrams(list_string: list[str], letter_bigram: str) -> bool:
    list_bigrams = [set(generate_letter_ngram(2, string))
                    for string in list_string]
    result = True
    for bigrams in list_bigrams:
        if letter_bigram not in bigrams:
            result = False
            break
    return result
