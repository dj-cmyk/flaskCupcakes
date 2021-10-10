from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class CupcakeForm(FlaskForm):
    '''docstring'''

    flavor = StringField('Flavor', 
                validators=[InputRequired()])
    size = SelectField('Size', 
                choices=[('small', 'small'), ('medium', 'medium'), ('large', 'large')])
    rating = FloatField('Rating', 
                validators=[Optional(), NumberRange(min=0, max=10)])
    image = StringField('Image URL Of Cupcake', 
                default="https://tinyurl.com/demo-cupcake", 
                validators=[URL(), Optional()])
    
    
