from flask import Flask, render_template

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

@app.route("/login")
def login():
    return render_template ("employee_login.html")

@app.route("/login2")
def login2():
    return render_template ("employer_login.html")


@app.route("/register")
def register():
    return render_template ("employee_register.html")

@app.route("/register2")
def register2():
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