from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, DecimalField, SelectField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileAllowed

class NewProperyForm(FlaskForm):
    title = StringField('Property Title', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    no_rooms = DecimalField('No. of Rooms', validators=[InputRequired()])
    no_bathrooms = DecimalField('No. of Bathrooms', validators=[InputRequired()])
    price = DecimalField('Price', validators=[InputRequired()])
    property_type = SelectField('Property Type', choices=[('House', "House"), ('Appartment', "Appartment"), ('Shared Space',"Shared Space")], validators=[])
    location = StringField('Location', validators=[InputRequired()])
    photo = FileField('Photo', validators=[InputRequired(), FileAllowed(['jpg', 'png'])])
