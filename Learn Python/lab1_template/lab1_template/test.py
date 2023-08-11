# # Django specific settings
# import inspect
# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
# from django.db import connection
# # Ensure settings are read
# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()

# # Your application specific imports
# from orm.models import User
# from datetime import date

# # Delete all data
# def clean_data():
#     User.objects.all().delete()

# # Test Django Model Setup
# def test_setup():
#     try:
#         clean_data()
#         # Create a test user and save to database
#         user = User(first_name='John', last_name='Doe', dob=date(1970, 3, 16))
#         user.save()
#         # Check user table is not empty
#         assert User.objects.count() > 0
#         print("Django Model setup completed.")
#     except AssertionError as exception:
#         print("Django Model setup failed with error: ")
#         raise(exception)
#     except:
#         print("Unexpected error")

# test_setup()

# import sqlite3

# conn = sqlite3.connect('emaildb.sqlite')
# cur = conn.cursor()

# # Create the Counts table if it doesn't exist already.
# cur.execute('DROP TABLE IF EXISTS Counts')
# cur.execute('''
# CREATE TABLE Counts (email TEXT, count INTEGER)''')

# # Read the mbox-short.txt file and count the number of times each email address appears.
# fname = input('Enter file name: ')
# if (len(fname) < 1): fname = 'mbox-short.txt'
# fh = open(fname)
# for line in fh:
#     if not line.startswith('From: '): continue
#     pieces = line.split()
#     email = pieces[1]
#     cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
#     row = cur.fetchone()
#     if row is None:
#         cur.execute('''INSERT INTO Counts (email, count)
#                 VALUES (?, 1)''', (email,))
#     else:
#         cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
#                     (email,))
#     conn.commit()

# # Get the top 10 email addresses with the most counts.
# sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

# for row in cur.execute(sqlstr):
#     print(str(row[0]), row[1])

# cur.close()

# ------------------------------------------------------------------------------

import sqlite3

conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Tracks')
cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')

# # conn.close()
# # --------------------------------------------------------------------------------------
# import sqlite3

# conn = sqlite3.connect('music.sqlite')
# cur = conn.cursor()

# cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', 
#     ('Thunderstruck', 20))
# cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', 
#     ('My Way', 15))
# conn.commit()

# print('Tracks:')
# cur.execute('SELECT title, plays FROM Tracks')
# for row in cur:
#         print(row)

# cur.execute('DELETE FROM Tracks WHERE plays < 100')
# conn.commit()

# cur.close()

# -----------------------------------------------------------
import sqlite3

conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Tracks')
cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')

cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', 
    ('Thunderstruck', 20))
cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', 
    ('My Way', 15))
conn.commit()

print('Tracks:')
cur.execute('SELECT title, plays FROM Tracks WHERE plays >= 1')
for row in cur:
        print(row)

cur.execute('DELETE FROM Tracks WHERE plays < 100')
conn.commit()

cur.close()


