# End Points

from flask import Flask, render_template, url_for, request, jsonify, flash, redirect


app = Flask(__name__, static_folder="assets", static_url_path="/assets")

app.secret_key = "some message or key"


# Url -> End Point
@app.route("/")
def hello_world():
    query = request.args.get("q")
    name = request.args.get("name", default="anonymous")
    subject = request.args.get("subject")
    
    print(query)
    print(name)
    print(subject)

    print(url_for("static", filename="style2.css"))
    return render_template("index.html", query=query, name=name, subject=subject)

@app.route("/prime")
def prime():
    return "<h1>Hello, From KK - Prime</h1>"


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form.get("username")
        password = request.form.get("password")

        print("Username:", name)

        friends = ["KK", "Karthik", "Kumar", "Karthikeyan"]

        header = "<header><h1>Welcome to the KK's website</h1></header>"

        # TODO: Verify the credentials against a database.
        return render_template("welcome.html", name=name, password=password, friends=friends, header=header)

    return render_template("login.html")
    

@app.route("/json")
def json():
    data = {
        "name": "KK",
        "age": 25,
        "city": "Chennai"
    }
    return jsonify(data), 200

@app.route("/hello2")
def hello_world2():
    
    return redirect(url_for("login"))

@app.route("/contact")
def contact():
    flash("Support is available 24/7. Please reach out to us for any assistance.")
    return render_template("contact.html")







if __name__ == "__main__":
    app.run(debug=True)