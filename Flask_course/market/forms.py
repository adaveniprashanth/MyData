from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from market.models import User
#the below fuunctions will provide the validation for conditions check
from wtforms.validators import Length,Email,DataRequired,EqualTo,ValidationError

class RegisterForm(FlaskForm):
    #inherited class Flaskform will exceute the functions starting with validate_  as prefix even if we dont call
    def validate_username(self,username_to_check):
        # print(type(username_to_check)) #its type is StringField not string
        user=User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError(f'User {username_to_check.data} is already exists.please try with different name')
    def validate_email(self,email_to_check):
        email=User.query.filter_by(email=email_to_check.data).first()
        if email:
            raise ValidationError(f'Email {email_to_check.data} is already exists.please try with different name')

    username=StringField(label='username',validators=[Length(min=2,max=30),DataRequired()])
    email=StringField(label='email',validators=[Email(),DataRequired()])
    password=PasswordField(label='password',validators=[Length(min=4,max=32),DataRequired()])
    confirm_password=PasswordField(label='Confirm password',validators=[EqualTo('password'),DataRequired()])
    submit=SubmitField(label='Submit')


class LoginForm(FlaskForm):
    email = StringField(label='email', validators=[Email(), DataRequired()])
    password = PasswordField(label='password', validators=[DataRequired()])
    submit = SubmitField(label='Login')


class PurchaseItemForm(FlaskForm):
    submit=SubmitField(label='Purchase')


class SellItemForm(FlaskForm):
    submit=SubmitField(label='SellItem')