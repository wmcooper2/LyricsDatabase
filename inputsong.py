#!/usr/bin/env python3
"""Test the inputting of a song into the database and which metrics are needed."""

import sqlite3
database = "songmetrics.db"
connection = sqlite3.connect(database)
db = connection.cursor()

# basic pattern
    # import sqlite3
    # make a connection
    # make a cursor to use the connection
    # the cursor is acted upon for all the execute commands
    # save any changes with connection.commit()
    # close access point with connection.close()

# create a table
    # db.execute()

# insert data 
    # db.execute()

# get data
    # db.execute()

# save the changes
    # connection.commit()

# close the database
    # connection.close()
