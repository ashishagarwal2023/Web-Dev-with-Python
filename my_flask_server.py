from flask import Flask, render_template

app = Flask(__name__)

name = "Ashish Agarwal"

@app.route('/')
def hello():
    return render_template("index.jinja", name=name)

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')