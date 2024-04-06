from flask import render_template, Flask

app = Flask(__name__)

name = "Ashish"

@app.route("/")
def index():
    return render_template("index.jinja", name=name)

@app.route("/rename")
def renameRoute():
    return "Hello world"

if __name__ == "__main__":
    app.run(debug=True)