from flask import Blueprint, redirect, render_template, url_for, current_app
from flask_wtf import FlaskForm
from wtforms import StringField

field_view_bp = Blueprint('field_view', __name__)

class StringForm(FlaskForm):
    name = StringField('name')

@field_view_bp.route('/string', methods=('GET', 'POST'))
def string():
    form = StringForm()
    if form.validate_on_submit():
        return render_template('field/string.html', form=form, success=True)
    return render_template('field/string.html', form=form)
