from flask import render_template, Flask, request, redirect
from html import escape

app = Flask(__name__)

name = "Ashish"

@app.route("/")
def index():
    return render_template("index.jinja", name=escape(name))

@app.route("/updateName", methods=["POST"])
def renameRoute():
    global name
    name = request.form.get("name")
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)