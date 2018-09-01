#!/usr/bin/env python3
"""Step 1, parse the text file into lines."""
from string import ascii_letters as alphabet

def print_elements(list_):
    for x in list_:
        if x != "":
            print(x)

def file_to_list(file_):
    """Each line in 'file_' becomes an element in a list. Returns List."""
    lines = []
    with open(file_, "r") as lyrics:
        for line in lyrics.readlines():
            lines.append(line.strip())
    return lines

def separate_by_spaces(line):
    """Splits words in 'line' at the spaces. Returns List."""
    words = []
    temp = list(line.split(" "))
    for word in temp:
        words.append(word.strip())
    return words

def remove_punctuation(word):
    """Removes punctuation from the word. Returns String.
        Doesn't remove "'"
    """
    good_punctuation = ["'"]
    no_punct = []
    for character in word:
        if character in alphabet or character in good_punctuation:
            no_punct.append(character)
    return ''.join(no_punct)

def remove_whitespace_from_word(element):
    """Removes all whitespace from 'element'. Returns String."""
    no_whitespace = []
    if element != "\n":
        for character in element:
            if character != "\n" and character != " ":
                no_whitespace.append(character)
    return "".join(no_whitespace).strip()

def remove_blank_elements(list_):
    """Removes all blank elements from 'list_'. Returns List."""
    temp = []
    for element in list_:
        if element != "\n" and element != "" and element != " ":
            temp.append(element)
    return temp

def remove_newlines(list_):
    """Removes all newlines from 'list_' elements. Returns List."""
    temp = []
    for element in list_:
        temp.append(element.strip())
    return temp

def remove_final_underscore(string):
    """Removes final underscore in 'string'. Returns String."""
    temp = []
    for character in string:
        if character != "_":
            temp.append(character)
    return ''.join(temp)

def remove_txt_suffix(string):
    """Removes the final '.txt' in the file name. Returns String."""
    temp = list(string)
    song_name = "".join(temp[:-4])     #remove ".txt"
    return song_name

#file_to_list()
#remove_blank_elements()
#separate_by_spaces()

