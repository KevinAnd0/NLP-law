from flask import Flask, json
from flask import jsonify, request
from flask.wrappers import Response
from werkzeug.wrappers import response
from nlpview import get_texts

app = Flask(__name__)

@app.route("/search/<phrase>", methods=["GET"])
def get_text_by_keyword(phrase):
    results = get_texts(phrase)
    JSONobject = jsonify(results)
    return JSONobject


app.run(port=1000, debug=True)
