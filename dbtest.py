#!/usr/bin/env python3
"""Insert all the songs into the database."""

import sqlite3
import metrics
from pathlib import Path

#import the database conection
def db_connect():
    """Connect to the database. Returns Cursor, Connection."""
    connection = sqlite3.connect("lyrics.db")
    db = connection.cursor()
    return db, connection

def db_maketable(db):
    """
    artistname      = text
    songname        = text
    link            = text, url
    genre           = ? maybe a list (songs can belong to more than one genre)
    wordcount       = integer
    linecount       = integer
    avgwordlen      = float, 4 digits
    avglinelen      = float, 4 digits
    maxwordlen      = integer
    minwordlen      = integer
    punctfreq       = a list of tuples (punc, freq)
    wordfreq        = a list of tuples (word, freq)
    """
    db.execute("CREATE TABLE songmetrics (artistname text, songname text, wordcount smallint, linecount smallint, avgwordlen float(4), avglinelen float(4), maxwordlen smallint, minwordlen smallint)") 

# make a generator for all the song files in the dir
def song_gen(song_dir):
    """Makes a generator of song files. Returns Generator."""
    for song in Path(song_dir).iterdir():
        yield str(song)
#for song in song_gen():        #checkpoint; path/generator works
#    print(song)

def db_insert(db, info):
    """Insert all the metrics into the database. Returns None."""
    db.execute("INSERT INTO songmetrics VALUES (?, ?, ?, ?, ?, ?, ?, ?)", 
                (info["artistname"], 
                 info["songname"], 
                 info["wordcount"], 
                 info["linecount"], 
                 info["avgwordlen"], 
                 info["avgwordsperline"], 
                 info["minwordlen"], 
                 info["maxwordlen"]))

def db_save(db):
    """Save the changes made to the database. Returns None."""
    db.commit()

def db_close(db):
    """Close the connection to the database. Returns None."""
    db.close()

def cut_string(gen):            #checkpoint; passing a generator works
    """testing the ability to pass a generator"""
    for x in gen():
        print(x[:-39])
#cut_string(song_gen)

database, connection = db_connect()
#db_maketable(database)         #only once, remake based on needed inputs, or add fields to all in the future(too much extra work)


song_dir = "/Users/wandalcooper/Programming/Github/Lyrics_Database/lyricstestdatabase/"
# analyze the song
for song_path in song_gen(song_dir):                    #when ready, point the gen at the 750,000 songs
    song_metrics = metrics.get_metrics(str(song_path))  #the song_path contains all the info for getting the metrics
    db_insert(database, song_metrics)

# checkpoint
#    print(  song_metrics["artistname"], 
#            song_metrics["songname"],
#            song_metrics["wordcount"], 
#            song_metrics["linecount"], 
#            song_metrics["avgwordlen"], 
#            song_metrics["avgwordsperline"], 
#            song_metrics["minwordlen"], 
#            song_metrics["maxwordlen"])

db_save(connection)
#db_close(connection)
