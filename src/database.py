#!/usr/bin/env python3
"""Insert all the songs into the database."""

import sqlite3
import metrics
from pathlib import Path

#import the database conection
def db_connect():
    """Connect to the database. Returns Cursor, Connection."""
    connection = sqlite3.connect("songs.db")
    db = connection.cursor()
    return db, connection

def db_maketables(db):
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
    db.execute("CREATE TABLE metrics (artistname text, songname text, wordcount smallint, linecount smallint, avgwordlen float(4), avglinelen float(4), maxwordlen smallint, minwordlen smallint)") 
#    db.execute("CREATE TABLE lyrics (artistname text, songname text, uniquewords array)")

def db_insert(db, data):
    """Insert all the metrics into the database. Returns None."""
    db.execute("INSERT INTO metrics VALUES (?, ?, ?, ?, ?, ?, ?, ?)", 
                (data["artistname"], 
                 data["songname"], 
                 data["wordcount"], 
                 data["linecount"], 
                 data["avgwordlen"], 
                 data["avgwordsperline"], 
                 data["minwordlen"], 
                 data["maxwordlen"]))


#connection.commit()

#connection.close()
