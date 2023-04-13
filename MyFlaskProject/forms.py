from flask_wtf import Form
from wtforms import IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from wtforms import validators, ValidationError
#import email_validator


class ContactForm(Form):
    name = TextAreaField("Candidate Name ", [validators.DataRequired("Please enter your name.")])
    Gender = RadioField('Gender', choices=[('M', 'Male'), ('F', 'Female')])
    Address = TextAreaField("Address")

    email = TextAreaField("Email", [validators.DataRequired("Please enter your email address.")])
    #email = TextAreaField("Email", [validators.DataRequired("Please enter your email address."),
    #                                validators.Email("Please enter your email address.")])

    Age = IntegerField("Age")
    language = SelectField('Programming Languages', choices=[('java', 'Java'), ('py', 'Python')])

    submit = SubmitField("Submit")