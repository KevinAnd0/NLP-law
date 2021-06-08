from flask import Flask, json
from flask import jsonify, request
from dbConnect import Database
from flask.wrappers import Response
from werkzeug.wrappers import response
from synScraper import get_syn

app = Flask(__name__)

@app.route("/search/<phrase>", methods=["GET"])
def get_text_by_keyword(phrase):
    db = Database()
    syns = get_syn(phrase)
    words = [db.get_keywords_by_search(s) for s in syns if db.get_keywords_by_search(s)]
    results = [db.get_texts_by_keywords(w.get('keyword')) for word in words for w in word if db.get_texts_by_keywords(w.get('keyword'))]
    JSONobject = jsonify(results)
    return JSONobject


app.run(port=1000, debug=True)
