import sqlite3
def connect():
    connection = sqlite3.connect("lyrics.db")
    db = connection.cursor()
    return db

#create table
db.execute("CREATE TABLE lyricstats (name text, link text, wordcount smallint)")

db.execute("INSERT INTO lyricstats VALUES ('song1','https://www.lyrics.com/song1',200)")

songs = []
for x in range(10):
    song = ("name"+str(x), "https://link"+str(x), x )
    songs.append(song)
    db.execute("INSERT INTO lyricstats VALUES (?,?,?)", song)
connection.commit()
#connection.close()
#db.executeall("INSERT INTO lyricstats VALUES (?,?,?)", songs)
