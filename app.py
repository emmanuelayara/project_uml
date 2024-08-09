import os
import random
from models import *
from settings import *
from forms import *
from flask import Flask, render_template, request, jsonify, redirect, url_for
from models import *



@app.route("/", methods=['GET'])
def newwave():
    return render_template ("newwave.html")


@app.route("/feed", methods=['GET'])
def feed():
        if request.method == "GET":
           return render_template ("feed.html")    

@app.route("/register", methods=["GET","POST"])
def register():
    form = UserForm()
    if request.method == "GET":
       return render_template ("employee_register.html", form=form)
    
    elif request.method == "POST":
        user_info = Users(
            email = form.email.data,
            password = form.password.data,
            first_name = form.first_name.data,
            last_name = form.last_name.data,
        )

        db.session.add(user_info)
        db.session.commit()

        message = "Welcome, {}".format(user_info.first_name)
        return redirect(url_for("user_login"))
    
    else:
        message = "Kindly select the correct request method"
        return jsonify(msg=message)

@app.route("/user_login", methods=['GET', 'POST'])
def user_login():
    form = UserForm()
    if request.method == 'GET':
        return render_template ("employee_login.html", form=form)

    elif request.method =="POST":
        email = form.email.data,
        password = form.password.data

        data = Users.query.get(email)
        if data:
            if data.password == password:
                return render_template("employee_profile.html",data=data)
            else:
                return ({"StatusCode": 401, "message": "Wrong username or password"})
        else:
            return jsonify({"StatusCode": 404, "Message": "User does not exist"})
        
    else:
        message = "Kindly select the correct request method"
        return jsonify(msg=message)
    
@app.route("/create_user_profile/<string:email>", methods=['GET', 'POST'])
def create_user_profile(email):
    form = UserForm()

    if request.method == "GET":
        return render_template("employee_profile.html", form=form)
    
    elif request.method=="POST":
        user_data = Profiles(
            profile_id = random.randint(1000, 10000),
            location = form.location.data,
            user_id = email,
        )
        
        db.session.add(user_data)
        db.session.commit()

        data = Users.query.get(email)
        return render_template("employee_profile.html", data=data)
    
@app.route("/user_profile/<string:email>/update", methods=['GET', 'PUT'])
def update_user_profile(email):
    form = UserForm()
    data = Users.query.get(email)

    if data:
        if request.method == "GET":
            return render_template("employee_profile.html", form=form,data=data)
        
        elif request.method =="PUT":
            profile = Profiles(
                location = form.location.data,
            )
            
            db.session.add(profile)
            db.session.commit()

            data = Users.query.get(email)
            return render_template("employee_profile.html", data=data)
    else:
        return jsonify({"StatusCode": 404, "Message": "User does not exist"})

@app.route("/user_account/<string:email>/delete", methods=['GET', 'DELETE'])
def delete_user_account(email):
    form = UserForm()
    data = Users.query.get(email)

    if request.method == 'GET':
        return render_template ("employee_login.html", form=form)

    elif request.method =="DELETE":
        password = form.password.data

        
        if data.password == password:
        
            db.session.delete(data)
            db.session.commit()
        return jsonify({"StatusCode": 200, "message": "Account deleted successfully"})

@app.route("/user_profile", methods=['GET'])
def user_profile(email):
    if request.method == "GET":
        data = Users.query.get(email)
        return render_template ("employee_profile.html", data=data)
        
@app.route("/employer_register", methods=["GET","POST"])
def employer_register():
    form = EmployerForm()
    if request.method == "GET":
       return render_template ("employer_register.html", form=form)
    
    elif request.method == "POST":
        employer_info = Employers(
            company_id = form.company_id.data,
            password = form.password.data,
            email = form.email.data,
            company_name = form.company_name.data,
            location = form.location.data,
            website = form.website.data
        )

        db.session.add(employer_info)
        db.session.commit()

        message = "Welcome, your ID is {}. Kindly keep it somewhere save as this is required for login".format(employer_info.company_id)
        return jsonify(msg=message)
    
    else:
        message = "Kindly select the correct request method"
        return jsonify(msg=message)

@app.route("/employer_login", methods=['GET', 'POST'])
def employer_login():
    form = EmployerForm
    if request.method == "GET":
        return render_template ("employer_login.html", form=form)

    elif request.method=="POST":
        company_id = form.username.data,
        password = form.password.data

        user = Users.query.get(company_id)
        if user.password == password:
            return render_template("employer_profile.html", data=user)
        
    else:
        message = "Kindly select the correct request method and try again"
        return jsonify(msg=message)


@app.route("/employer_profile", methods=['POST'])
def employer_profile():
    return render_template ("employer_profile.html")


@app.route("/create_employer_profile", methods=['POST'])
def create_employer_profile():
    return render_template ("create_employer_profile.html")


@app.route("/jobs", methods=['GET','POST'])
def jobs():
    return render_template ("jobs.html")

@app.route("/network", methods=['GET','POST'])
def network():
    return render_template ("network.html")


@app.route("/notifications", methods=['GET','POST'])
def notifications():
    return render_template ("notifications.html", methods=['GET'])

if __name__== "__main__":
    app.run(host="0.0.0.0", debug=True)