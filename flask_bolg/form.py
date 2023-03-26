from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_bolg import db
from wtforms import StringField, PasswordField, SubmitField,BooleanField,IntegerField,RadioField
from flask_login import current_user
from wtforms.validators import DataRequired, Length,EqualTo,ValidationError
from flask import flash
#from app import Person
class RegistrationForm(FlaskForm):
    username=StringField('username',validators=[DataRequired(),Length(min=2, max=20)],render_kw={"placeholder":"username"})
    userfname=StringField('userfname',validators=[DataRequired(),Length(min=2, max=20)],render_kw={"placeholder":"userFname"})
    usergfname=StringField('usergfname',validators=[DataRequired(),Length(min=2, max=20)],render_kw={"placeholder":"userFname"})
    userage=IntegerField('age',validators=[DataRequired()])
    usergender=RadioField('gender',choices=['male','female'])
    userphone_number=StringField('phone_number',validators=[DataRequired(),Length(min=2, max=16)])
    userCountry=StringField('userCountry',validators=[DataRequired()])
    password=PasswordField('Password',validators=[DataRequired()])
    confirm_password=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('signup')
    def validate_username(self, username):
        from flask_bolg.model import User
        user=User.query.filter_by(user_name=username.data).first()
        if user:
            raise ValidationError('the username is taken .please choose a different one.')
    def validate_userphone_number(self, userphone_number):
        from flask_bolg.model import User
        user=User.query.filter_by(user_phone_number=userphone_number.data).first()
        if user:
            raise ValidationError('the phone_number is taken .please choose a different one.') 
        
class wish_Form(FlaskForm): 
    submit=SubmitField('add to wish list')       


class update_Form(FlaskForm):
    username=StringField('username',validators=[DataRequired(),Length(min=2, max=20)],render_kw={"placeholder":"username"})
    userphone_number=StringField('phone_number',validators=[DataRequired(),Length(min=2, max=16)])
    picture=FileField('Update profile picture',validators=[FileAllowed(['jpg','png'])])
    cover_picture=FileField('Update cover picture',validators=[FileAllowed(['jpg','png'])])
    submit=SubmitField('update')
    def validate_username(self, username):
        from flask_bolg.model import User
        if current_user.user_name!=username.data:
            user=User.query.filter_by(user_name=username.data).first()
            if user:
                flash('the username is taken ')
    def validate_userphone_number(self, userphone_number): 
        from flask_bolg.model import User               
        if current_user.user_phone_number!=userphone_number.data:
            user=User.query.filter_by(user_phone_number=userphone_number.data).first()
            if user:
                flash('the phone number is taken ')            

class SearchForm(FlaskForm):
    search=StringField("Searched",validators=[DataRequired()])
    submit=SubmitField("submit")


class LoginForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired(),Length(min=2, max=20)],render_kw={"placeholder":"username"})
    password=PasswordField('Password',validators=[DataRequired()])
    remember=BooleanField('Remember Me')
    submit=SubmitField('Login')
        
    