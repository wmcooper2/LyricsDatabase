#!/usr/bin/env python3
"""Analyzes the song and extracts metrics for lyrics.db"""

import re
import string
from pathlib import Path
from parselyrics import remove_punctuation as rmv_punct
from parselyrics import file_to_list
from parselyrics import separate_by_spaces
from parselyrics import remove_whitespace_from_word as rmv_wht_wrd
from parselyrics import remove_blank_elements as rmv_blnk_elmt
from parselyrics import remove_newlines as rmv_nwln
from parselyrics import remove_final_underscore as rmv_undrscr
from parselyrics import remove_txt_suffix as rmv_sfx

all_ascii = string.ascii_letters + string.digits + string.punctuation # + string.whitespace

#not used
def artist_name(string):
    """Extracts the artist's name from 'string'. Returns String."""
    elements = Path(string).parts
    name_element = elements[-1]
    match = re.match(".*[_$]", name_element)    #matches up to the underscore
    name = rmv_undrscr(match[0])
    return name

def artist_and_song_names(string):
    """Extracts the artist and song name from the string. Returns Strings."""
    elements = Path(string).parts
    name_elements = elements[-1]            
    if name_elements.count("_") == 1:
        names = name_elements.split("_")    #split into artist name and song name
    else:
        raise Exception("More or less than one underscore")
    song_name = rmv_sfx(names[1])
    return names[0], song_name

def link(x):
    """Gets the url for the song. Returns String."""
    pass

def word_count(list_):
    """Counts the number of words in 'file_'. Returns Integer.
       Doesn't count whitespaces as words.
    """
    words = []
    for line in list_:
        for word in line.split(" "):
            word = rmv_wht_wrd(word)
            word = rmv_punct(word)
            words.append(word.strip())
    return len(words)

def unique_word_count(list_):
    """Gets the total amount of unique words in the list. Returns Integer."""
    return list(set(list_))

def line_count(list_):
    """Counts the number of lines in 'file_'. Returns Integer.
       Doesn't include newline spaces (blank lines).
    """
    temp = rmv_nwln(list_)
    temp = rmv_blnk_elmt(temp)
    return len(temp)

def add_digits(word):
    """Counts the digits in the word. Returns Integer."""
    return sum(1 for character in word)

def average_word_len(list_, wordcount):
    """Gets an average length of the words in 'list_'. Returns Float."""
    digitcount = 0
    for line in list_:
        for word in line.split():
            word = rmv_punct(word)
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
                word = rmv_wht_wrd(word)
                word = rmv_punct(word)
                length = len(word)
                if length > max_len:
                    max_len = length
                if length < min_len:
                    min_len = length
    return min_len, max_len

def ascii_counter(text_file):
    """Counts all the individual characters in 'text_file'. Returns Dictionary."""
    letter_dict = {}
    for letter in all_ascii:
        letter_dict[letter] = 0
    for line in text_file.readlines():
        for word in line.split():
            for character in word:
                if character in all_ascii:
                    letter_dict[character] += 1
    return letter_dict

def get_metrics(song_path):
    """Get all the metrics from a song. Returns Dictionary.
        type(song_path) == str
    """
    with open(song_path, "r") as song:
#        ascii_chars = ascii_counter(song)           #count all the non-whitespace ascii characters
#        for key, value in ascii_chars.items():
#            print(key, value)

        song_list = file_to_list(song_path)         #split the file into lines

        # tokenize by word
        song_words = []
        for line in song_list:
            line_words = separate_by_spaces(line)   #split the line into words
            for word in line_words:
                song_words.append(word)

        # remove punctuation that the dictionary doesn't like
        punct_removed = []                          # remove bad punctuation
        for word in song_words:
            punct_removed.append(rmv_punct(word))

        songtext = song.readlines()
        artistname, songname = artist_and_song_names(song_path)
        wordcount = word_count(songtext)
        linecount = line_count(songtext)
        avgwordlen = average_word_len(songtext, wordcount)
        avgwordsperline = average_words_per_line(linecount, wordcount)
        minwordlen, maxwordlen = word_len(songtext)
        # unique words count
        # dict of unique words and their counts
        # unique letters count (some songs may not use some letters)
        # dict of unique letters and thier counts
        # unique punctuation count
        # dict of unique punctuation and their counts
        
        metrics = {}
        metrics["artistname"]       = artistname 
        metrics["songname"]         = songname
        metrics["wordcount"]        = wordcount
        metrics["linecount"]        = linecount
        metrics["avgwordlen"]       = avgwordlen
        metrics["avgwordsperline"]  = avgwordsperline
        metrics["minwordlen"]       = minwordlen
        metrics["maxwordlen"]       = maxwordlen

        return metrics, set(song_words)

# pass the file path to parselyrics.py, then to metrics.py. 
# 1st - parse the lyrics (read file, break up lines and words, remove punctuation)
# 2nd - gather the metrics on each song (read file again, count things, calculate averages)

# for now, just use these metrics to start.
# later, use the expand function in the database to add more fields then run those metrics on all the songs.
##    artistname      = text
##    songname        = text
#    link            = text, url
##    wordcount       = integer
##    linecount       = integer
##    avgwordlen      = float, 4 digits
##    avglinelen      = float, 4 digits
##    maxwordlen      = integer
##    minwordlen      = integer
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
# count how many letters of each in the lyrics; {a:111, b:76, c:32 ...}
# make a json dict with words and their frequency
# how many words appear in the Merriam-Webster dictionary
# words that are poetic uses of the word
# words that are created by that artist
# words that are slang
# (some words are all caps and may need to be lowered; some proper nouns)
# genre
# weeks on hits chart


#artist metrics
# length of song name
# length of artist name
# average length of song names
# average length of artist names
#

