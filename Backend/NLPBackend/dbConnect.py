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
'''


'''
Methods:

- Text - table

get_all_rows_in_texts() - Gets all rows in the text field
get_text_by_id(id) - Gets text by id


- Keywords - table

get_all_keywords() - Gets all rows in keywords
get_specific_keyword(word) - Finds all posts with a specific word

'''


class Database:

    def __init__(self):
        self.db_name = "nlpdatabase.db"
        self.connection = sqlite3.connect(self.db_name)
        self.cur = self.connection.cursor()

    def get_all_rows_in_texts(self):
        results = []
        for row in self.cur.execute('''SELECT * FROM texts'''):
            obj = {
                self.cur.description[0][0]: row[0],
                self.cur.description[1][0]: row[1],
                self.cur.description[2][0]: row[2]
            }
            results.append(obj)
        return results

    def get_text_by_id(self, id):
        self.cur.execute("SELECT * FROM texts where id = ?",(id,))
        result = self.cur.fetchone()
        return result

    def get_all_keywords(self):
        results = []
        for row in self.cur.execute('''SELECT * FROM keywords'''):
            obj = {
                self.cur.description[0][0]: row[0],
                self.cur.description[1][0]: row[1]
            }
            results.append(obj)
        return results

    def get_specific_keyword(self, word):
        results = []
        self.cur.execute("SELECT * FROM keywords WHERE keyword = ?",(word,))
        rows = self.cur.fetchall()
        for row in rows:
            results.append(row)
        return results

    def get_keywords_by_search(self, word):
        results = []
        self.cur.execute("SELECT * FROM keywords WHERE LOWER(keyword) LIKE ('%'||?||'%')", (word,))
        rows = self.cur.fetchall()
        for row in rows:
            obj = {
                self.cur.description[0][0]: row[0],
                self.cur.description[1][0]: row[1]
            }
            results.append(obj)
        return results

    def get_texts_by_keywords(self, keyword):
        results = None
        check = self.cur.execute('''SELECT DISTINCT * FROM texts JOIN keywords, keywordsXtexts
                            ON texts.id = keywordsXtexts.texts AND keywords.id = keywordsXtexts.keywords 
                            WHERE LOWER(keywords.keyword) = ?''', (keyword,))
        rows = self.cur.fetchall()
        for row in rows:
            results = {
                self.cur.description[0][0]: row[0],
                self.cur.description[1][0]: row[1],
                self.cur.description[2][0]: row[2]
            }
        return results
    
    def close(self):
        self.connection.commit()
        self.connection.close()

