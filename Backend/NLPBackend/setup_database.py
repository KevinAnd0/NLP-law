import os
import sqlite3
import spacy

# 'scraped' är ca 100 textfiler av rubriker från olika mål (ifall vi inte inkluderar dessa filer i GitHub)
dir_path = os.getcwd()
path_to_scraped = rf'NLP-law\Backend\NLPBackend\scraped'
path_to_pipeline = rf'{dir_path}\NLP-law\Backend\NLPBackend\sv_pipeline-0.0.0\sv_pipeline\sv_pipeline-0.0.0'
# Load small english model: https://spacy.io/models
nlp=spacy.load(path_to_pipeline)

def delete_database():
    con = sqlite3.connect(r'NLP-law/Backend/NLPBackend/nlpdatabase.db')
    cur = con.cursor()

    cur.execute("DELETE FROM keywordsXtexts")
    con.commit()
    cur.execute("DELETE FROM keywords")
    con.commit()
    cur.execute("DELETE FROM texts")
    con.commit()
    

    con.close()


def get_keywords(text):
    pos_tag = ['NOUN']
    key_words = []
    doc = nlp(text)
    for token in doc:
        if(token.is_stop or token.is_punct):
            continue
        elif(token.pos_ in pos_tag):
            key_words.append(token.lemma_)
    
    # Get rid of duplicates
    key_words = list(set(key_words))
            
    return key_words

def setup_database():
    con = sqlite3.connect(r'NLP-law/Backend/NLPBackend/nlpdatabase.db')
    cur = con.cursor()

    file_names = os.listdir(path_to_scraped)
    file_id = 1
    for f in file_names:
        file = open(os.path.join(path_to_scraped, f)).read()
        text = file.split(':')
        
        keywords_from_text = []
        referat = ""
        for i in range(len(text)):
            if "Rubrik" in text[i]:
                referat = str(text[i+1][:-8])
                keywords_from_text = get_keywords(referat)
                break
            
        # Add the summary and the link (which I currently don't have access to) in the database
        # At first, the summary is just going to be the 'rubriker' text.
        cur.execute("INSERT INTO texts (id, summary) VALUES (?, ?)", (file_id, referat))
        con.commit()

        ######
        # Get all the existing keywords in the database
        cur.execute('SELECT keyword FROM keywords')
        result = cur.fetchall()
        db_keywords = [k[0] for k in result]


        for word in keywords_from_text:
            # Check if the keyword already exist in the database. If not, insert the word.
            if word not in db_keywords:
                cur.execute("INSERT INTO keywords (keyword) VALUES (?)", (word,))
                con.commit()
            
            # Retrieve the id for the keyword
            cur.execute('SELECT id FROM keywords WHERE keyword == (?)', (word,))
            id = int(cur.fetchone()[0])

            # Add to the cross table
            cur.execute("INSERT INTO keywordsXtexts (keywords, texts) VALUES (?,?)", (id, file_id))
            con.commit()

        file_id += 1

    con.close()


# setup_database()

# delete_database()