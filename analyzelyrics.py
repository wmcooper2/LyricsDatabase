#!/usr/bin/env python3
"""This module handles the loading of the song files."""

from pathlib import Path
from metrics import get_metrics
from database import db_maketable, db_insert, db_connect

lyrics_dir = "/Users/wandalcooper/Programming/Github/Lyrics_Database/testlyrics/"
db, connection = db_connect()
try:
    db_maketable(db)
except:
    print("Table in database already exists...skipping")

# analyze the song, point at the dir with 750000 songs
songs = Path(lyrics_dir).iterdir()              #iterate through the directory with the song files
for each_song in songs:
    song_metrics = get_metrics(each_song)       #'each_song' is an absolute path
    db_insert(db, song_metrics)
    connection.commit()

#    print(song_metrics["artistname"], 
#          song_metrics["songname"],
#          song_metrics["wordcount"], 
#          song_metrics["linecount"], 
#          song_metrics["avgwordlen"], 
#          song_metrics["avgwordsperline"], 
#          song_metrics["minwordlen"], 
#          song_metrics["maxwordlen"])

# user feedback
#    print("IN DATABASE ::", each_song.parts[-1])


###### check the unique word set using Merriam-Webster API
# later this is important when searching 

# when all songs are finished, or if error count exceeds 3:
connection.close()
