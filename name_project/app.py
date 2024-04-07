from flask import render_template, Flask, request

app = Flask(__name__)

name = "Ashish"

@app.route("/")
def index():
    return render_template("index.jinja", name=name)

@app.route("/rename", methods=["POST"])
def renameRoute():
    global name
    name = request.form.get("name")
    return name

if __name__ == "__main__":
    app.run(debug=True)