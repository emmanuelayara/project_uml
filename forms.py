from flask_wtf import Form
from wtforms import StringField, SelectField, TextAreaField, IntegerField, DateField, EmailField, validators, ValidationError  
from wtforms.validators import DataRequired, AnyOf, URL 
from wtforms import SubmitField, RadioField, SelectField  
  


class EmployeeProfileForm(Form):  
   name = TextAreaField("Name")
   address = TextAreaField("Address")  
   email = TextAreaField("Email")    
   profession = TextAreaField("Profession")
   college = TextAreaField("College")
   submit = SubmitField("Submit")


class EmployeeLoginForm(Form):
    username = StringField("Username", validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")



class ItemForm(Form):
    username = StringField(
    )
    email = EmailField(
        "email", validators=[DataRequired()]
    )
    password = StringField(
        "password", validators=[DataRequired()]
    )