
# sql.py - Create an SQLite3 table and populate it with data


import sqlite3

# create a new database if the db doesn't already exist
with sqlite3.connect("blog.db") as conn:

	# get a cursor
	c = conn.cursor()

	# create the table
	c.execute("""CREATE TABLE posts
		(title text, post text)
		""")

	# insert dummy data into the table
	c.execute('INSERT INTO posts values ("Good", "I\'m good.")')
	c.execute('INSERT INTO posts values ("well", "I\'m well.")')
	c.execute('INSERT INTO posts values ("Excellent", "I\'m exellent.")')
