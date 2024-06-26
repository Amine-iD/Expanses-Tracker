from flask_wtf import FlaskForm 
from wtforms import StringField , PasswordField , EmailField , SubmitField,ValidationError 
from wtforms.validators import DataRequired , Length , Email ,EqualTo

class Register(FlaskForm):    

    def validate_user_name(self , user_name_to_check):
        from tracker.dbmodels import User 
        user = User.query.filter_by(user_name = user_name_to_check.data).first()
        if user :
                raise ValidationError("User name already exists , Please try another one!")
    def validate_email(self , email_to_check):
          from tracker.dbmodels import User
          email = User.query.filter_by(email = email_to_check.data).first()
          if email:
                raise ValidationError("Email adress already exists! Please try a different one ")
    
    user_name = StringField(label='User Name :' , validators = [Length(min=5 , max=15) , DataRequired()])
    email = EmailField(label = 'Email :' , validators = [Length(min=6 , max=25) , Email()])
    password1 = PasswordField(label='Password :' , validators = [Length(min=7) , DataRequired()])
    password2 = PasswordField(label='Confirm Password :', validators = [EqualTo('password1') , DataRequired()])
    submit = SubmitField(label='Create Account')

class Login(FlaskForm):
    
    user_name = StringField(label='Name :' , validators = [Length(min=5 , max=15) , DataRequired()])
    password = PasswordField(label='Password :' , validators = [Length(min=7) , DataRequired()])
    submit = SubmitField(label='Login')
    
class AddCategory(FlaskForm):
    def validate_category_name(self , category_to_check):
        from tracker.dbmodels import Category
        category = Category.query.filter_by(category_name = category_to_check.data).first()
        if category:
             raise ValidationError('Category already exists!')     
    
    category_name = StringField(label='Category' , validators=[DataRequired()])
    submit = SubmitField(label='Add Category') 

class DeleteCategory(FlaskForm):
     ...
