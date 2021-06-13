import requests
import re
from dbConnect import Database


def get_syn(query):
    response = requests.get(f'https://www.synonymer.se/sv-syn/{query}')
    syn_tags = re.findall(r'<li value="1">(.+?)</li>', response.text)    
    syns = re.findall(r'sv-syn/(.+?)">', syn_tags[0])
    syns.insert(0, query)
    return syns


def get_texts(phrase):
    db = Database()
    syns = get_syn(phrase)
    words = [db.get_keywords_by_search(s) for s in syns if db.get_keywords_by_search(s)]
    results = [db.get_texts_by_keywords(w.get('keyword')) for word in words for w in word if db.get_texts_by_keywords(w.get('keyword'))]
    db.close()
    return results

