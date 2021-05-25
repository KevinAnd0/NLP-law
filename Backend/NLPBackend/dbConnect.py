import sqlite3

'''
Usage:
The class initializes a connection by default.
The class methods use this when you call the methods.

In the API, you define an object and connect to the database
through that object.
For example:
    databasCon = Database()
    databaseCon.get_all_rows_in_texts()
    databaseCon.close()
    
(Always close the connection after use)

Methods:

- Text - table

get_all_rows_in_texts() - Gets all rows in the text field


- Keywords - table
get_all_keywords() - Gets all rows in keywords
get_specific_keyword(word) - Finds all posts with a specific word

'''


class Database:

    def __init__(self):
        self.db_name = "nlpdatabase.db"
        self.connection = sqlite3.connect(self.db_name)

    def get_all_rows_in_texts(self):
        rows = []
        self.cur = self.connection.cursor()
        for row in self.cur.execute('''SELECT * FROM texts'''):
            rows.append(row)
        return rows

    def get_all_keywords(self):
        rows = []
        self.cur = self.connection.cursor()
        for row in self.cur.execute('''SELECT * FROM keywords'''):
            rows.append(row)
        return rows

    def get_specific_keyword(self,word):
        results = []
        self.cur = self.connection.cursor()
        self.cur.execute("SELECT * FROM keywords WHERE keyword = ?",(word,))
        rows = self.cur.fetchall()
        for row in rows:
            results.append(row)
        return results

    def close(self):
        self.connection.commit()
        self.connection.close()