import sqlite3


db_name = "nlpdatabase.db"

connection = sqlite3.connect(db_name)

cur = connection.cursor()

for row in cur.execute('''SELECT * FROM texts'''):
    print(row)

connection.commit()
connection.close()