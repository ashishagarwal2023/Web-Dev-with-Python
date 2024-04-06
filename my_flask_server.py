from flask import Flask, render_template

app = Flask(__name__)

shopItems = [
    {"name": "Ceramic Mug", "stock": 20, "price": 5.99},
    {"name": "Stainless Steel Water Bottle", "stock": 15, "price": 12.49},
    {"name": "Wooden Picture Frame", "stock": 25, "price": 8.99},
    {"name": "Fancy Pen Set", "stock": 30, "price": 14.99},
    {"name": "Scented Candle", "stock": 40, "price": 7.99}
]

iLikeChocolate = False

name = "Ashish Agarwal"

@app.route('/')
def hello():
    return render_template("index.jinja", name=name, fruits=["Apple", "Mango", "Banana", "Orange", "Grapes"], choco=iLikeChocolate, shopItems=shopItems)

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')