#the flask import function "jsonify" was not recognized by the flask module
#pip installed json, unfortunately, this didn't work either
#pressed pause on this one for now and went to other API open source practice projects

import flask
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Home"

if __name__ == "__main__":
    app.run(debug=True)