from flask import Flask, json
from flask import jsonify, request
from dbConnect import Database
from flask.wrappers import Response
from werkzeug.wrappers import response
from synScraper import get_syn

app = Flask(__name__)


@app.route("/texts", methods=["GET"])
def get_all_text_urls():
    db = Database()
    all_rows = db.get_all_rows_in_texts()
    json_object = jsonify(all_rows)
    db.close()
    return json_object



@app.route("/texts/<int:id>", methods=["GET"])
def get_text_by_id(id):
    db = Database()
    text = db.get_text_by_id(id)
    JSONobject = jsonify(text)
    db.close()
    return JSONobject


@app.route("/keywords", methods=["GET"])
def get_all_keywords():
    db = Database()
    keywords = db.get_all_keywords()
    JSONobject = jsonify(keywords)
    db.close()
    return JSONobject


@app.route("/keywords/<word>")
def get_specific_keyword(word):
    db = Database()
    keywords = db.get_specific_keyword(word)
    JSONobject = jsonify(keywords)
    db.close()
    return JSONobject


@app.route("/search/<word>", methods=["GET"])
def get_text_by_keyword(word):
    db = Database()
    syns = get_syn(word)
    syns.insert(0, word)
    words = [db.get_keywords_by_search(s) for s in syns if db.get_keywords_by_search(s)]
    results = []
    for wor in words:
        for w in wor:
            obj = db.get_texts_by_keywords(w.get('keyword'))
            results.append(obj)
    JSONobject = jsonify(results)
    return JSONobject
    

app.run(port=1000, debug=True)
