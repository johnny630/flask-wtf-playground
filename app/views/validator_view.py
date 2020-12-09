
from flask import Blueprint, request, render_template
from flask_wtf import FlaskForm
# wtform
from wtforms import BooleanField, IntegerField, PasswordField, SubmitField, StringField
from wtforms.validators import (
    DataRequired, Email, Length, EqualTo, InputRequired, IPAddress, MacAddress, NumberRange,
    Optional, Regexp, URL, UUID, AnyOf, NoneOf, ValidationError
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


class NumberRangeForm(FlaskForm):
    number = IntegerField('Number', [NumberRange(10, 50)])

@validator_view_bp.route('/number_range', methods=('GET', 'POST'))
def number_range():
    form = NumberRangeForm()

    if request.method == 'POST' and form.validate_on_submit():
        return render_template('validator/number_range.html', form=form, success=True)

    return render_template('validator/number_range.html', form=form)


class OptionalForm(FlaskForm):
    age = IntegerField('age', [Optional()])

@validator_view_bp.route('/option', methods=('GET', 'POST'))
def option():
    form = OptionalForm()

    if request.method == 'POST' and form.validate_on_submit():
        return render_template('validator/option.html', form=form, success=True)

    return render_template('validator/option.html', form=form)


class RegexpForm(FlaskForm):
    regexp = StringField('regexp', [Regexp('^\w{2,3}$')])

@validator_view_bp.route('/regexp', methods=('GET', 'POST'))
def regexp():
    form = RegexpForm()

    if request.method == 'POST' and form.validate_on_submit():
        return render_template('validator/regexp.html', form=form, success=True)

    return render_template('validator/regexp.html', form=form)


class URLForm(FlaskForm):
    url = StringField('url', [URL()])

@validator_view_bp.route('/url', methods=('GET', 'POST'))
def url():
    form = URLForm()

    if request.method == 'POST' and form.validate_on_submit():
        return render_template('validator/url.html', form=form, success=True)

    return render_template('validator/url.html', form=form)

class UUIDForm(FlaskForm):
    uuid = StringField('uuid', [UUID()])

@validator_view_bp.route('/uuid', methods=('GET', 'POST'))
def uuid():
    form = UUIDForm()
    import uuid

    uuid = str(uuid.uuid4())

    if request.method == 'POST' and form.validate_on_submit():
        return render_template('validator/uuid.html', form=form, uuid=uuid, success=True)

    return render_template('validator/uuid.html', uuid=uuid, form=form)


class AnyOfForm(FlaskForm):
    choose = StringField('choose a number 1 to 3', [AnyOf(('1', '2', '3'))])

@validator_view_bp.route('/any_of', methods=('GET', 'POST'))
def any_of():
    form = AnyOfForm()

    if request.method == 'POST' and form.validate_on_submit():
        return render_template('validator/any_of.html', form=form,success=True)

    return render_template('validator/any_of.html', form=form)

class NoneOfForm(FlaskForm):
    choose = StringField('choose a number without 1 to 3', [NoneOf(('1', '2', '3'))])

@validator_view_bp.route('/none_of', methods=('GET', 'POST'))
def none_of():
    form = NoneOfForm()

    if request.method == 'POST' and form.validate_on_submit():
        return render_template('validator/none_of.html', form=form,success=True)

    return render_template('validator/none_of.html', form=form)

####################
# Custom validators
def check_age(form, field):
        if field.data < 13:
            raise ValidationError("We're sorry, you must be 13 or older to register")

# Instead, we can turn our validator into a more powerful one by making it a factory which returns a callable:
def length_method(min=-1, max=-1):
    message = 'Must be between %d and %d characters long.' % (min, max)

    def _length(form, field):
        l = field.data and len(field.data) or 0
        if l < min or max != -1 and l > max:
            raise ValidationError(message)

    return _length

# class wrap
class LengthClass(object):
    def __init__(self, min=-1, max=-1, message=None):
        self.min = min
        self.max = max
        if not message:
            message = u'Field must be between %i and %i characters long.' % (min, max)
        self.message = message

    def __call__(self, form, field):
        l = field.data and len(field.data) or 0
        if l < self.min or self.max != -1 and l > self.max:
            raise ValidationError(self.message)

class InLineValidatorForm(FlaskForm):
    name = StringField('Name', [InputRequired()])
    nick_name = StringField('Nick name', [InputRequired(), length_method(min=2, max=10)])
    mobile = StringField('mobile', [InputRequired(), LengthClass(min=8, max=10)])
    age = IntegerField('Age', [InputRequired(), check_age])

    # In-line Validators method name: validate_fieldname
    def validate_name(form, field):
        if len(field.data) > 10:
            raise ValidationError('Name must be less than 10 characters')

@validator_view_bp.route('/custom', methods=('GET', 'POST'))
def custom():
    form = InLineValidatorForm()

    if request.method == 'POST' and form.validate_on_submit():
        return render_template('validator/custom.html', form=form,success=True)

    return render_template('validator/custom.html', form=form)
    