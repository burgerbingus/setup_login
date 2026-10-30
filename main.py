from flask import Flask, request, redirect
from database import Database
import config

app = Flask(__name__)

db = Database()

@app.route("/")
def home():
    return """
    <h1>My Task Manager</h1>
    <a href='/login'>Login</a>
    <a href='/tasks'>Tasks</a>
    """

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        result = db.login(username, password)

        if result:
            return "Welcome back!"

        return "Wrong username or password"

    return """
    <form method="POST">
        Username: <input name="username">
        Password: <input name="password" type="password">
        <input type="submit">
    </form>
    """

@app.route("/tasks")
def tasks():
    all_tasks = db.get_tasks()

    output = "<h1>My Tasks</h1>"

    for task in all_tasks:
        output += "<p>" + str(task[1]) + "</p>"

    return output

@app.route("/add", methods=["POST"])
def add_task():
    task = request.form["task"]
    db.add_task(task)

    return redirect("/tasks")


if __name__ == "__main__":
    app.run(debug=config.DEBUG)
