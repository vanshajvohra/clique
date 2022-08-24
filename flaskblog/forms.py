from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    gender = StringField('Gender',
                         validators=[DataRequired(), Length(min=1, max=8)])
    age = IntegerField('Age',
                       validators=[DataRequired()])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()

        if username.data == 'admin':
            raise ValidationError('Cannot set name to admin')

    def validate_gender(self, gender):
        if (gender.data != 'Male' and gender.data != 'male' and gender.data != 'Female' and gender.data != 'female' and gender.data != 'Trans' and gender.data != 'trans'):
            raise ValidationError('Gender can be Male/Female/Trans')

    def validate_age(self, age):
        if (age.data < 0 or age.data > 99):
            raise ValidationError(
                'Age cannot be negative or more than 99 years')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                'That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class AdminviewForm(FlaskForm):
    #email = StringField('Email',
    #                    validators=[DataRequired(), Email()])

    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Get Service Records')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    gender = StringField('Gender',
                         validators=[DataRequired(), Length(min=1, max=8)])
    age = IntegerField('Age',
                       validators=[DataRequired()])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[
                        FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()

        if username.data == 'admin':
            raise ValidationError('Cannot set name to admin')

    def validate_gender(self, gender):
        if (gender.data != 'Male' and gender.data != 'male' and gender.data != 'Female' and gender.data != 'female' and gender.data != 'Trans' and gender.data != 'trans'):
            raise ValidationError('Gender can be Male/Female/Trans')

    def validate_age(self, age):
        if (age.data < 0 or age.data > 99):
            raise ValidationError(
                'Age cannot be negative or more than 99 years')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError(
                    'That email is taken. Please choose a different one.')


class PostForm(FlaskForm):
    # title = StringField('Title', validators=[DataRequired()])
    # content = TextAreaField('Content', validators=[DataRequired()])

    car_model = StringField('Model', validators=[DataRequired()])
    car_make = StringField('Make', validators=[DataRequired()])
    purchase_year = IntegerField(
        'Year of Purchase', validators=[DataRequired()])
    km_done = IntegerField('Kilometres Covered', validators=[DataRequired()])
    dealership = StringField('Name of Mechanic/Repair Shop Last Visited',
                             validators=[DataRequired()])
    date_last_visit = DateField(
        'Date of Last Visit', validators=[DataRequired()])

    reason = TextAreaField('Reason for Last Visit',
                           validators=[DataRequired()])

    city = StringField('City', validators=[DataRequired()])
    province = StringField('Province', validators=[DataRequired()])

    submit = SubmitField('Post')


class ServicereqForm(FlaskForm):
    # title = StringField('Title', validators=[DataRequired()])
    # content = TextAreaField('Content', validators=[DataRequired()])

    car_model = StringField('Model', validators=[DataRequired()])
    car_make = StringField('Make', validators=[DataRequired()])
    purchase_year = IntegerField(
        'Year of Purchase', validators=[DataRequired()])
    km_done = IntegerField('Kilometres Covered', validators=[DataRequired()])
    dealership = StringField('Name of Mechanic/Repair Shop Last Visited',
                             validators=[DataRequired()])
    date_last_visit = DateField(
        'Date of Last Visit', validators=[DataRequired()])

    reason = TextAreaField('Reason for Last Visit',
                           validators=[DataRequired()])

    city = StringField('City', validators=[DataRequired()])
    province = StringField('Province', validators=[DataRequired()])


class RequestResetForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError(
                'There is no account with that email. You must register first.')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')
