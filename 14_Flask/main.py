# End Points
from flask import Flask

app = Flask(__name__)


# Url -> End Point
@app.route("/")
def hello_world():
    return "<h1>Hello, From KK</h1>"

@app.route("/prime")
def prime():
    return "<h1>Hello, From KK - Prime</h1>"

if __name__ == "__main__":
    app.run(debug=True)