from flask_wtf import Form
from wtforms import StringField, SelectField, TextAreaField, IntegerField, DateField, EmailField, validators, ValidationError  
from wtforms.validators import DataRequired, AnyOf, URL 
from wtforms import SubmitField, RadioField, SelectField  
  


class ProfileForm(Form):  
   name = TextAreaField("name")
   Address = TextAreaField("Address")  
   email = TextAreaField("Email")    
   Profession = TextAreaField("profession")
   college = TextAreaField("college")
   submit = SubmitField("Submit")

class ItemForm(Form):
    username = StringField(
    )
    email = EmailField(
        "email", validators=[DataRequired()]
    )
    password = StringField(
        "password", validators=[DataRequired()]
    )