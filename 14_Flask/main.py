# End Points
from flask import Flask, render_template

app = Flask(__name__)


# Url -> End Point
@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/prime")
def prime():
    return "<h1>Hello, From KK - Prime</h1>"


@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)