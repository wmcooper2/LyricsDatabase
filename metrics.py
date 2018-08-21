#!/usr/bin/env python3
"""Analyzes the song and extracts metrics for lyrics.db"""

import re
from pathlib import Path
from string import ascii_letters as alphabet

def remove_punctuation(word):
    """Removes punctuation from the word. Returns String.
        Doesn't remove "'" and "-"
    """
    good_punctuation = ["'", "-"]
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

def artist_name(string):
    """Extracts the artist's name from 'path_object'. Returns String."""
    elements = Path(string).parts
    name_element = elements[-1]
    match = re.match(".*[_$]", name_element)    #matches up to the underscore
    def remove_final_underscore(string):
        """Removes final underscore in 'string'. Returns String."""
        temp = []
        for character in string:
            if character != "_":
                temp.append(character)
        return ''.join(temp)
    name = remove_final_underscore(match[0])
    return name

def song_name(x):
    return name

def link(x):
    return link

def word_count(list_):
    """Counts the number of words in 'file_'. Returns Integer.
       Doesn't count whitespaces as words.
    """
    words = []
    for line in list_:
        for word in line.split(" "):
            word = remove_whitespace_from_word(word)
            word = remove_punctuation(word)
            words.append(word.strip())
    return len(words)

def line_count(list_):
    """Counts the number of lines in 'file_'. Returns Integer.
       Doesn't include newline spaces (blank lines).
    """
    temp = remove_newlines(list_)
    temp = remove_blank_elements(temp)
    return len(temp)

def add_digits(word):
    """Counts the digits in the word. Returns Integer."""
    return sum(1 for character in word)

def average_word_len(list_, wordcount):
    """Gets an average length of the words in 'list_'. Returns Float."""
    digitcount = 0
    for line in list_:
        for word in line.split():
            word = remove_punctuation(word)
            digitcount += add_digits(word)
    return round(digitcount/wordcount, 2)

def average_words_per_line(linecount, wordcount):
    """Gets an average length of the lines in words. Returns Float.
       Doesn't include whitespace and punctuation.

        examples:
            "I like birds." -> "Ilikebirds"
            " join the party! And, " -> "jointhepartyAnd"
    """
    return round(wordcount/linecount, 2)

def average_digits_per_line(list_):
    """Gets an average length of the lines in digits. Returns Float.
       Doesn't include whitespace and punctuation.

        examples:
            "I like birds." -> "Ilikebirds"
            " join the party! And, " -> "jointhepartyAnd"
    """
    pass

def word_len(list_):
    """Determines the longest word. Returns Integer.
       Doesn't count whitespaces and punctuation.
    """
    max_len = 0
    min_len = 100
    for line in list_:
        for word in line.split(" "):
            if word != "\n":
                word = remove_whitespace_from_word(word)
                word = remove_punctuation(word)
                length = len(word)
                if length > max_len:
                    max_len = length
                if length < min_len:
                    min_len = length
    return min_len, max_len

            


#    artistname      = text
#    songname        = text
#    link            = text, url
#    genre           = ?
##    wordcount       = integer
##    linecount       = integer
##    avgwordlen      = float, 4 digits
##    avglinelen      = float, 4 digits
##    maxwordlen      = integer
##    minwordlen      = integer
#    punctfreq       = a list of tuples (punc, freq)
#    wordfreq        = a list of tuples (word, freq)


#other possible metrics:
# punctuation per line
# average punctuation per line
# how many questions in a song
# how many all caps letters
# how many lowercase letters
# length of song name
# length of artist name
# longest line length
# shortest line length
# longest word length
# shortest word length
# the longest word(s) (list)
# the shortest word(s) (list)

#artist metrics
# length of song name
# length of artist name
# average length of song names
# average lenght of artist names
#




def get_metrics(song_path):
    """Gather all metrics into one list. Returns List.
        type(song_path) == str
    """
    with open(song_path, "r") as song:
        songtext = song.readlines()
        artistname = artist_name(song_path)
        wordcount = word_count(songtext)
        linecount = line_count(songtext)
        avgwordlen = average_word_len(songtext, wordcount)
        avgwordsperline = average_words_per_line(linecount, wordcount)
        minwordlen, maxwordlen = word_len(songtext)
        
        metrics = {}
        metrics["artistname"] = artistname 
        metrics["wordcount"] = wordcount
        metrics["linecount"] = linecount
        metrics["avgwordlen"] = avgwordlen
        metrics["avgwordsperline"] = avgwordsperline
        metrics["minwordlen"] = minwordlen
        metrics["maxwordlen"] = maxwordlen

#        return [wordcount, linecount, avgwordlen, avgwordsperline, minwordlen, maxwordlen, artistname]

        return metrics
