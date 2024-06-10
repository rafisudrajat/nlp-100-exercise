"""
Problem:

Split the sentence “Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics”. 
into words, and create a list whose element presents the number of alphabetical letters in the corresponding word.
"""


def split_word_count_char(sentence:str)->list[int]:
    char_count_in_words=[]
    char_counter=0
    for char in sentence:
        if (ord(char)>=65 and ord(char)<=90) or (ord(char)>=97 and ord(char)<=122):
            char_counter+=1
        if ord(char)==32:
            char_count_in_words.append(char_counter)
            char_counter=0
    char_count_in_words.append(char_counter)
    return char_count_in_words