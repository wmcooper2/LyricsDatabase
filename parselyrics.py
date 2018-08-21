#!/usr/bin/env python3
"""Step 1, parse the text file into lines."""

def print_elements(list_):
    for x in list_:
        if x != "":
            print(x)
print("lines ::")
lyric_file = "/Users/wandalcooper/Desktop/testlyrics.txt"
lines = []

with open(lyric_file, "r") as lyrics:
    for line in lyrics.readlines():
        lines.append(line.strip())
print_elements(lines)

words = []
for line in lines:
    temp = list(line.split(" "))
    for word in temp:
        words.append(word.strip())
print("words ::")
print_elements(words)

set_ = set(words)
print_elements(set_)
# remove !  ,  ...   ?    punctuations
# use existing punctuation removal function

# make a json dict with words and their frequency
# insert into database using sqlite3

