from flask_wtf import FlaskForm
from wtforms import StringField, FileField, DecimalField, \
    SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, IPAddress, InputRequired, \
    EqualTo, Email


class CompanyForm(FlaskForm):
    """
    Company form
    """
    name = StringField('Name',
                       validators=[DataRequired(), Length(min=2, max=255)])
    submit = SubmitField('Submit')


class CompanyLocationForm(FlaskForm):
    """
    Company Location form
    """
    name = StringField('Name',
                       validators=[DataRequired(), Length(min=2, max=255)])
    address = StringField('Address',
                          validators=[DataRequired(), Length(min=2, max=255)])
    city = StringField('City',
                       validators=[DataRequired(), Length(min=2, max=255)])
    state = StringField('State',
                        validators=[DataRequired(), Length(min=2, max=255)])
    zipcode = StringField('Zipcode',
                          validators=[DataRequired(), Length(min=2, max=255)])
    phone = StringField('Phone',
                        validators=[DataRequired(), Length(min=2, max=255)])
    fax = StringField('Fax')
    email = StringField('Email')
    submit = SubmitField('Submit')


class CompanyPrinterForm(FlaskForm):
    """
    Company Printer form
    """
    name = StringField('Name',
                       validators=[DataRequired(), Length(min=2, max=255)])
    ip = StringField('IP Address',
                     validators=[DataRequired(), IPAddress()])
    port = IntegerField('Port',
                        validators=[DataRequired()])
    type = SelectField('Type',
                       choices=[('receipt', 'Receipt'),
                                ('kitchen', 'Kitchen'),
                                ('bar', 'Bar')])
    submit = SubmitField('Submit')


class MenuForm(FlaskForm):
    """
    Form to add/edit a menu.
    """
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Submit')


class MenuItemForm(FlaskForm):
    """
    Form to add/edit a menu item.
    """
    name = StringField('Name', validators=[DataRequired()])
    price = DecimalField('Price', validators=[DataRequired()])
    submit = SubmitField('Submit')


class PagerForm(FlaskForm):
    """
    Form to change the number of items per page.
    """
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Add Pager')


class IngredientForm(FlaskForm):
    """
    Form to add/edit an ingredient.
    """
    name = StringField('Name', validators=[DataRequired()])
    price = DecimalField('Price')
    submit = SubmitField('Submit')
