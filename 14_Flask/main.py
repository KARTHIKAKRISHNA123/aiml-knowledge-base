# End Points
from flask import Flask, render_template, url_for, request

app = Flask(__name__, static_folder="assets", static_url_path="/assets")


# Url -> End Point
@app.route("/")
def hello_world():
    print(url_for("static", filename="style2.css"))
    return render_template("index.html")

@app.route("/prime")
def prime():
    return "<h1>Hello, From KK - Prime</h1>"


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
            print(request.form)
            name = request.form["username"]
            password = request.form["password"]
            print(name, password)
    
            # send it to database and check if user exists or not(verify user)
            return f"<p>Username: {name}</p><p>Password: {password} and this is post method</p>"
    else:
        return render_template("login.html")




if __name__ == "__main__":
    app.run(debug=True)