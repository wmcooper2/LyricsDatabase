#!/usr/bin/env python3
"""Insert all the songs into the database."""

import sqlite3
import metrics
from pathlib import Path

#import the database conection
def db_connect():
    connection = sqlite3.connect("lyrics.db")
    db = connection.cursor()
    return db, connection

def db_maketable(db):
    """
    artistname      = text
    songname        = text
    link            = text, url
    genre           = ?
    wordcount       = integer
    linecount       = integer
    avgwordlen      = float, 4 digits
    avglinelen      = float, 4 digits
    maxwordlen      = integer
    minwordlen      = integer
    punctfreq       = a list of tuples (punc, freq)
    wordfreq        = a list of tuples (word, freq)
    """
    db.execute("CREATE TABLE songmetrics (artistname text, songname text, link text, wordcount smallint, linecount smallint, avgwordlen float(4), avglinelen float(4), maxwordlen smallint, minwordlen smallint, punctcount smallint, wordfreq multiset)") 

# make a generator for all the song files in the dir
song_dir = "/Users/wandalcooper/Programming/Github/Lyrics_Database/lyricstestdatabase/"
def song_gen():
    for song in Path(song_dir).iterdir():
        yield str(song)
#for song in song_gen():        #checkpoint; path/generator works
#    print(song)

def db_insert(info):
    db.execute("INSERT INTO songmetrics VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", info)

def db_save(db):
    db.commit()

def db_close(db):
    db.close()

def cut_string(gen):            #checkpoint; passing a generator works
    """testing passing a generator"""
    for x in gen():
        print(x[:-39])
#cut_string(song_gen)



# analyze the song
for song_path in song_gen():
    song_metrics = metrics.get_metrics(str(song_path))          #the song_path contains all the info for getting the metrics

#    print(song_metrics[6], 
#            "words::", song_metrics[0], 
#            "lines::", song_metrics[1], 
#            "avgwordlen::", song_metrics[2],
#            "avgwordsperline::", song_metrics[3],
#            "minwordlen::", song_metrics[4],
#            "maxwordlen::", song_metrics[5],)

    print(  song_metrics["artistname"], 
            song_metrics["wordcount"], 
            song_metrics["linecount"], 
            song_metrics["avgwordlen"], 
            song_metrics["avgwordsperline"], 
            song_metrics["minwordlen"], 
            song_metrics["maxwordlen"])






#database, connection = db_connect()
#db_maketable(database)         #only once
#db_save(connection)
#db_close(connection)
