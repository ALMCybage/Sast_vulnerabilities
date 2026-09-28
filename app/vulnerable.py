from flask import Flask, request
import sqlite3
import os

app = Flask(__name__)

@app.route("/user")
def user():

    user_id = request.args.get("id")

    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()

    # SQL Injection
    query = "SELECT * FROM users WHERE id = " + user_id
    cursor.execute(query)

    return "Done"


@app.route("/cmd")
def cmd():

    command = request.args.get("cmd")

    # Command Injection
    os.system(command)

    return "Executed"


@app.route("/echo")
def echo():

    message = request.args.get("q", "")

    # Reflected XSS
    return f"<html><body><h1>{message}</h1></body></html>"


if __name__ == "__main__":
    app.run()