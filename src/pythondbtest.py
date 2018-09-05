import sqlite3
from pprint import pprint
connection = sqlite3.connect("songs.db")
db = connection.cursor()
db.execute("CREATE TABLE metrics (artistname text, songname text, wordcount integer)")
#db.execute("INSERT INTO metrics VALUES('Frank Sinatra', 'New York, New York', 170)")

my_data = [("New York, New York", "Frank Sinatra", 170),
           ("Mack the Knife", "Louis Armstrong", 155),
           ("Bohemian Rhapsody", "Queen", 377)]

for record in my_data:
    db.execute("INSERT INTO metrics (songname, artistname, wordcount) VALUES(?, ?, ?)", (record[0], record[1], record[2]))


connection.commit()
connection.close()

connection = sqlite3.connect("songs.db")
db = connection.cursor()
my_record = db.execute("select * from metrics")
pprint(my_record.fetchall())
connection.close()
