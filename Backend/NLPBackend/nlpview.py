from synScraper import get_syn
from dbConnect import Database

def get_texts(phrase):
    db = Database()
    syns = get_syn(phrase)
    words = [db.get_keywords_by_search(s) for s in syns if db.get_keywords_by_search(s)]
    results = [db.get_texts_by_keywords(w.get('keyword')) for word in words for w in word if db.get_texts_by_keywords(w.get('keyword'))]
    db.close()
    return results