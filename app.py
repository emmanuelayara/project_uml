from flask import Flask, render_template, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from models import Users
from forms import ItemForm
from settings import app, db
import random
import os


app = Flask(__name__)
jwt = JWTManager(app)


class Profile:
    def __init__(self, name, profession, college, year_of_graduation, course, skills, previous_jobs):
        self.name = name
        self.profession = profession
        self.college = college
        self.year_of_graduation = year_of_graduation
        self.course = course
        self.skills = skills
        self.previous_jobs = previous_jobs


@app.route("/register")
def register():
    form = ItemForm()

    if request.method == "POST":
        user_info = Users(
            password = request.json.get("password"),
            email = request.json.get("email")
        )

        db.session.add(user_info)
        db.session.commit()

        message = "Welcome, your user ID is {}. Kindly keep it somewhere save as this is required for login".format(id)
        access_token = create_access_token(identity=id)
        return jsonify(access_token=access_token,msg=message), 201


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

@app.route("/employee_profile")
def employee_profile():
    return render_template ("employee_profile.html")
    

@app.route("/create_employee_profile")
def create_employee_profile():
    return render_template ("create_employee_profile.html")

@app.route("/employer_profile")
def employer_profile():
    return render_template ("employer_profile.html")

@app.route("/create_employer_profile")
def create_employer_profile():
    return render_template ("create_employer_profile.html")

@app.route("/network")
def network():
    return render_template ("network.html")

@app.route("/notifications")
def notifications():
    return render_template ("notifications.html")

if __name__== "__main__":
    app.run(host="0.0.0.0", debug=True)