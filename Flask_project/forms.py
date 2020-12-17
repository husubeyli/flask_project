from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, SubmitField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, Email


class LoginForm(FlaskForm):
    username = StringField(label='İstifadəçi adı', validators=[DataRequired(), Length(min=3, max=30)])
    password = PasswordField(label='Parol', validators=[DataRequired(), Length(min=8, max=30)])

class CommentForm(FlaskForm):
    user_name = StringField('Tam adınız: ', validators=[DataRequired()])
    comment = TextAreaField('Şərhiniz: ', validators=[DataRequired()])
    start = DateField('Start Date', format='%m/%d/%Y')
    submit = SubmitField("Submit")


class RegisterForm(FlaskForm):
    first_name = StringField(label='Ad', validators=[DataRequired(), Length(min=3, max=30)])
    last_name = StringField(label='Soyad', validators=[DataRequired(), Length(min=3, max=30)])
    email = EmailField(label='Email', validators=[DataRequired(), Length(min=3, max=30)])
    username = StringField(label='İstifadəçi adı', validators=[DataRequired(), Length(min=3, max=30)])
    password = PasswordField(label='Parol', validators=[DataRequired(), Length(min=8, max=30)])

