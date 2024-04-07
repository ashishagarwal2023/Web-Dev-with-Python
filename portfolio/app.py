from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.jinja")

@app.route("/about")
def aboutMe():
    return render_template("about.jinja")

if __name__ == "__main__":
    app.run(debug=True)