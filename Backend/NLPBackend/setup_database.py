# This file is here in case the database needs to be generated from scratch again. 
# The files 'scraped', 'pdfs', are not in Github. Also, 'scraped' has been sligthly modified
# from its original form due to some minor issues.

import os
import sqlite3
import spacy

# 'scraped' has 164 text files of summaries of judicial precedent cases concerning consumer rights
# 'pdfs' has 146 pdfs of detailed descriptions of the various cases. Not all cases located in 'scraped' 
# has one of these descriptions.

dir_path = os.getcwd()

path_to_scraped = rf'{dir_path}\NLP-law\Backend\NLPBackend\scraped'

path_to_pipeline = rf'{dir_path}\NLP-law\Backend\NLPBackend\sv_pipeline-0.0.0\sv_pipeline\sv_pipeline-0.0.0'
nlp=spacy.load(path_to_pipeline)

# Load up the filenames of the directories 'pdfs' and 'scraped' to two lists
# Extract their corresponding case number.
list_of_info = os.listdir(path_to_scraped)
list_of_info = [j[4:-4] for j in list_of_info]
list_of_referat = os.listdir(rf'{dir_path}\NLP-law\Backend\NLPBackend\pdfs')
list_of_referat = [j[:-4] for j in list_of_referat]


# Finally, compare and figure out which cases lack 'referat'
cases_with_no_ref = [j for j in list_of_info if (j not in list_of_referat)]


def delete_database():
    con = sqlite3.connect('nlpdatabase.db')
    cur = con.cursor()

    # Each table is emptied. Tables are not dropped in order to keep their settings,
    # which was set manually in the beginning.
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
    con = sqlite3.connect('nlpdatabase.db')
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
        
        # Getting rid of 'mål_' in the beginning of the filename and '.txt' in the end.
        link = f[4:-4]
        if link in cases_with_no_ref:
          cur.execute("INSERT INTO texts (id, summary) VALUES (?, ?)", (file_id, referat))
        else:
          link = f'{link}.pdf'
          cur.execute("INSERT INTO texts (id, documentlink, summary) VALUES (?, ?, ?)", (file_id, link, referat))
        
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



# Uncomment the function that is needed below
# Multiple '#':s to avoid accidents:

####### setup_database()

####### delete_database()