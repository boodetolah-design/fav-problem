import sqlite3

conn = sqlite3.connect("fav.db")

n = conn.cursor()

fav = input("fav: ").capitalize()

n.execute("SELECT COUNT (*) AS a FROM fav WHERE problem = ?", (fav,))
row = n.fetchone()
if row:
    print(row[0])

conn.close()