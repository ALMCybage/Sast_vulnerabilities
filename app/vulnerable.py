from flask import Flask, request
import sqlite3
import os
import subprocess

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


@app.route("/file")
def file_read():

    filename = request.args.get("name", "")

    # Path Traversal
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


@app.route("/run")
def run():

    command = request.args.get("cmd", "")

    # Command Injection (shell=True)
    output = subprocess.check_output(command, shell=True, text=True)

    return output


if __name__ == "__main__":
    app.run()
