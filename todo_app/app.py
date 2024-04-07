from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

todo = {
    "Something" : {
        "name": "Something",
        "done": True,
    }
}

@app.route("/")
def index():
    return render_template("index.jinja", items=todo.values())

@app.route("/addTodo", methods=["POST"])
def addTodo():
    global todo
    todoName = request.form.get("todoName")
    todo[todoName] = {"name": todoName, "done": False}
    return redirect(url_for("index"))

@app.route("/done/<task>", methods=["POST", "GET"])
def markDone(task):
    task = request.view_args.get("task")
    todo[task]["done"] = True
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
    
    
    