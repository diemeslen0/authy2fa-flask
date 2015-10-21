from flask_wtf import Form
from wtforms import IntegerField, PasswordField, StringField, validators

from ..models import User


def validate_unique_email(form, field):
    """Validates that an email address hasn't been registered already"""
    if User.query.filter_by(email=field.data).count() > 0:
        raise validators.ValidationError('This email address has already been registered.')

class SignUpForm(Form):

    name = StringField('Full name', validators=[validators.InputRequired()])
    email = StringField('Email', validators=[validators.InputRequired(), validate_unique_email])
    password = PasswordField('Password', validators=[validators.InputRequired()])
    country_code = IntegerField('Country code', validators=[validators.InputRequired()])
    phone_number = StringField('Mobile phone', validators=[validators.InputRequired()])
