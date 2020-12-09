from flask import Blueprint, request, redirect, render_template, url_for, current_app
from flask_wtf import FlaskForm
from wtforms import fields
from wtforms.fields import html5

field_view_bp = Blueprint('field_view', __name__)

class StringForm(FlaskForm):
    name = fields.StringField('name')

@field_view_bp.route('/string', methods=('GET', 'POST'))
def string():
    form = StringForm()
    if form.validate_on_submit():
        return render_template('field/string.html', form=form, success=True)
    return render_template('field/string.html', form=form)


class BasicForm(FlaskForm):
    boolean = fields.BooleanField('boolean')
    date = fields.DateField('date')
    date_time = fields.DateTimeField('date_time')
    decimal = fields.DecimalField('decimal')
    file = fields.FileField('file')
    multiple_file = fields.MultipleFileField('multiple_file')
    float = fields.FloatField('float')
    integer = fields.IntegerField('integer')
    radio = fields.RadioField('radio', choices=['a', 'b', 'c'])
    #DOTO: Select fields with dynamic choice values
    select = fields.SelectField('select', choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')])
    select_multiple = fields.SelectMultipleField('select_multiple', choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')])
    string = fields.StringField('string')
    hidden = fields.HiddenField('hidden')
    password = fields.PasswordField('password')
    text_area = fields.TextAreaField('text_area')

    search = html5.SearchField('search')
    tel = html5.TelField('tel')
    url = html5.URLField('url')
    email = html5.EmailField('email')
    html5_date_time = html5.DateTimeField('html5_date_time')
    html5_date = html5.DateField('html5_date')
    time = html5.TimeField('time')
    date_time_local = html5.DateTimeLocalField('date_time_local')
    html5_integer = html5.IntegerField('html5_integer')
    html5_decimal = html5.DecimalField('html5_decimal')
    integer_range = html5.IntegerRangeField('integer_range')
    decimal_range = html5.DecimalRangeField('decimal_range')
    

    submit = fields.SubmitField('Submit')

@field_view_bp.route('/basic', methods=('GET', 'POST'))
def basic():
    form = BasicForm()

    if request.method == 'POST' and form.validate_on_submit():
        return render_template('field/basic.html', form=form, success=True)

    return render_template('field/basic.html', form=form)
