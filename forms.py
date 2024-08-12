from flask_wtf import Form
from wtforms import StringField, SelectField, TextAreaField, IntegerField, DateField, EmailField, validators, ValidationError  
from wtforms.validators import DataRequired, AnyOf, URL 
from wtforms import SubmitField, RadioField, SelectField  
  

class UserForm(Form):  
   first_name = StringField("First Name", validators=[DataRequired()])
   last_name = StringField("Last Name", validators=[DataRequired()])
   password = StringField("Password", validators=[DataRequired()])
   email = StringField("Email", validators=[DataRequired()])
   location = StringField("Address")      
   bio = TextAreaField("Bio")
   skills = StringField("Skills")
   role = StringField("Role")
   year_of_graduation = IntegerField("Year of Graduation")
   profile_id = StringField("profile_id")


class EmployerForm(Form):
    company_id = StringField("Company ID", validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired()])
    company_name = StringField("Company Name", validators=[DataRequired()])
    email = StringField("Email")
    location = SelectField("Location")
    website = StringField("Website")
    

class JobForm(Form):
    company_id = IntegerField("Job id")
    title = StringField("Title")
    description = StringField("Description")
    location = SelectField("Location")
    salary = StringField("Salary")
    job_type = StringField('employment_type')
