from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password')
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign in')

class TopCities(FlaskForm):
   city_name = StringField('City Name', validators=[DataRequired()])
   city_rank = IntegerField('City Rank', validotors=[DataRequired()]) 
   is_visited = BooleanField('Visited')
   submit = SubmitField('Submit')
