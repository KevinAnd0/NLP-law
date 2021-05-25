from flask import Flask
from flask import jsonify, request
from dbConnect import Database

app = Flask(__name__)


@app.route("/texts", methods=["GET"])
def get_all_text_urls():
    db = Database()
    all_rows = db.get_all_rows_in_texts()
    json_object = jsonify(all_rows)
    db.close()
    return json_object

@app.route("/keywords")
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



app.run(debug=True)
