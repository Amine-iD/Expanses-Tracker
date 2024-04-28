from flask_wtf import FlaskForm 
from wtforms import StringField , PasswordField , EmailField , SubmitField 
from wtforms.validators import DataRequired , Length , Email ,EqualTo

class Register(FlaskForm):
    user_name = StringField(label='User Name' , validators = [Length(min=5 , max=15) , DataRequired()])
    email = EmailField(label = 'Email' , validators = [Length(min=6 , max=25) , Email()])
    password1 = PasswordField(label='Password' , validators = [Length(min=7) , DataRequired()])
    password2 = PasswordField(label='Confirm Password', validators = [EqualTo('password1') , DataRequired()])
    submit = SubmitField(label='Create Account')

