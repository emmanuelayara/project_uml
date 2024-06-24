import os
import random
from models import *
from settings import *
from forms import ItemForm
from flask import Flask, render_template, request, jsonify
from models import Users, Applications, Jobs, Notifications, Employers, Profiles, Admin



@app.route("/")
def newwave():
    return render_template ("newwave.html")


@app.route("/feed")
def feed():
    return render_template ("feed.html")    

@app.route("/jobs", methods=['GET'])
def view_jobs():
    return render_template ("jobs.html")

@app.route("/employee_login")
def employee_login():
    return render_template ("employee_login.html")

@app.route("/employer_login")
def employer_login():
    return render_template ("employer_login.html")


@app.route("/employee_register", methods=["GET","POST"])
def employee_register():
    if request.method == "GET":
        return render_template ("employee_register.html")
    elif request.method == "POST":
        company_id = random.randint(1000000, 1999999)
        employer_info = Employers(
            company_id = company_id,
            password = request.json.get("password"),
            email = request.json.get("email"),
            company_name = request.json.get("company_name"),
        )

        db.session.add(employer_info)
        db.session.commit()

        message = "Welcome, your ID is {}. Kindly keep it somewhere save as this is required for login".format(company_id)
        return jsonify(msg=message), 201

@app.route("/employer_register", methods=["GET","POST"])
def employer_register():
    return render_template ("employer_register.html")

@app.route("/employee_profile")
def employee_profile():
    return render_template ("employee_profile.html")

@app.route("/create_employee_profile", methods=['GET', 'POST'])
def create_employee_profile():
    form = ProfileForm()
    if request.method=="POST":
        print("name:",form.name.data)
        print("Address:",form.Address.data)
        print("Email:",form.email.data)
        print("profession:",form.Profession.data)
        Print("college:",form.college.data)
    return render_template ("create_employee_profile.html", form=form)

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