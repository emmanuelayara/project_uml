from flask import Flask, render_template
from settings import app, db
from models import Users


app = Flask(__name__)

@app.route("/")
def newwave():
    return render_template ("newwave.html")

@app.route("/feed")
def feed():
    return render_template ("feed.html")

@app.route("/jobs")
def jobs():
    return render_template ("jobs.html")

@app.route("/employee_login")
def employee_login():
    return render_template ("employee_login.html")

@app.route("/employer_login")
def employer_login():
    return render_template ("employer_login.html")


@app.route("/employee_register")
def employee_register():
    return render_template ("employee_register.html")

@app.route("/employer_register")
def employer_register():
    return render_template ("employer_register.html")

@app.route("/profile")
def profile():
    return render_template ("profile.html")

@app.route("/network")
def network():
    return render_template ("network.html")

@app.route("/notifications")
def notifications():
    return render_template ("notifications.html")

if __name__== "__main__":
    app.run(host="0.0.0.0", debug=True)