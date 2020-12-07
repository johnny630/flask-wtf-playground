import os

from flask import Blueprint, redirect, render_template, url_for, current_app
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField
from wtforms.validators import DataRequired
from werkzeug.utils import secure_filename

index_bp = Blueprint('index', __name__)


class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])

@index_bp.route('/submit', methods=('GET', 'POST'))
def submit():
    form = MyForm()
    if form.validate_on_submit():
        return 'success'

    return render_template('submit.html', form=form)


class PhotoForm(FlaskForm):
    photo = FileField(validators=[FileRequired()])

@index_bp.route('/upload', methods=['GET', 'POST'])
def upload():
    form = PhotoForm()
    if form.validate_on_submit():
        f = form.photo.data
        filename = secure_filename(f.filename)
        f.save(os.path.join(
            current_app.root_path, 'photos', filename
        ))
        return 'success'

    return render_template('upload.html', form=form)
