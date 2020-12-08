
from flask import Blueprint, request, render_template
from flask_wtf import FlaskForm
# wtform
from wtforms import BooleanField, IntegerField, PasswordField, SubmitField, StringField
from wtforms.validators import (
    DataRequired, Email, Length, EqualTo, InputRequired, IPAddress, MacAddress
)

validator_view_bp = Blueprint('validator_view', __name__)

class DataRequiredForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    level = IntegerField('level', validators=[DataRequired()])
    submit = SubmitField('Go')

@validator_view_bp.route('/data_required', methods=('GET', 'POST'))
def data_required():
    form = DataRequiredForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            return render_template('validator/data_required.html', form=form, success=True)
        else:
            return 'post fail'

    return render_template('validator/data_required.html', form=form)


class EmailForm(FlaskForm):
    email = StringField('email', validators=[Email(), Length(min=10, max=100)])
    submit = SubmitField('Submit')

@validator_view_bp.route('/email', methods=('GET', 'POST'))
def email():
    form = EmailForm()

    if request.method == 'POST' and form.validate_on_submit():
        return render_template('validator/email.html', form=form, success=True)

    return render_template('validator/email.html', form=form)


class EqualToForm(FlaskForm):
    password = PasswordField('New Password', [InputRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm  = PasswordField('Repeat Password')
    submit = SubmitField('Submit')

@validator_view_bp.route('/equal_to', methods=('GET', 'POST'))
def equal_to():
    form = EqualToForm()

    if request.method == 'POST' and form.validate_on_submit():
        return render_template('validator/equal_to.html', form=form, success=True)

    return render_template('validator/equal_to.html', form=form)


class IPAddressForm(FlaskForm):
    ip = StringField('IP Address', [InputRequired(), IPAddress()])
    submit = SubmitField('Submit')

@validator_view_bp.route('/ip_address', methods=('GET', 'POST'))
def ip_address():
    form = IPAddressForm()

    if request.method == 'POST' and form.validate_on_submit():
        return render_template('validator/ip_address.html', form=form, success=True)

    return render_template('validator/ip_address.html', form=form)


class MacAddressForm(FlaskForm):
    mac = StringField('Mac Address', [MacAddress()])
    submit = SubmitField('Submit')

@validator_view_bp.route('/mac_address', methods=('GET', 'POST'))
def mac_address():
    form = MacAddressForm()

    if request.method == 'POST' and form.validate_on_submit():
        return render_template('validator/mac_address.html', form=form, success=True)

    return render_template('validator/mac_address.html', form=form)