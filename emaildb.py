import sqlite3

# Establish a connection to the SQLite database and create a cursor
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

# Drop the 'Counts' table if it exists and create a new one
cur.execute('''DROP TABLE IF EXISTS Counts''')
cur.execute('''CREATE TABLE Counts (email TEXT, count INTEGER)''')

# Prompt the user for the input file name (defaulting to 'mbox-short.txt' if not provided)
fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'

# Open and read the input file
fh = open(fname)
for line in fh:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    email = pieces[1]

    # Execute a SELECT query to check if the email address exists in the database
    cur.execute('SELECT count from Counts WHERE email = ? ', (email,))
    row = cur.fetchone()

    if row is None:
        # If the email address is not in the database, insert a new row with count = 1
        cur.execute('''INSERT INTO Counts(email, count) VALUES (?, 1)''', (email,))
    else:
        # If the email address is in the database, update the count
        cur.execute('UPDATE Counts set count = count + 1 WHERE email = ?', (email,))
        conn.commit()  # Commit the changes to the database

# Construct an SQL query to retrieve the top 10 email addresses by count
sqlstr = 'SELECT email, count from Counts ORDER BY count DESC LIMIT 10'

# Execute the query and print the results
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

# Close the cursor and the database connection
cur.close()
