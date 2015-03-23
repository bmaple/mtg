from flask.ext.wtf import Form
from wtforms import TextField, validators, SubmitField
class RegistrationForm(Form):
        username = TextField('Username', [validators.Length(min=4, max=25)])
        #email = TextField('Email Address', [validators.Length(min=6, max=35)])
        submit = SubmitField('submit')
