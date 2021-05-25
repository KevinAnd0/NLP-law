from flask import Flask
app = Flask(__name__)

@app.route("/")
def entrypoint():
    return "hello"

app.run()