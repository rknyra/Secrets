from flask_wtf import FlaskForm
from wtforms import SelectField,StringField,TextAreaField,SubmitField
from wtforms.validators import Required
from wtforms import ValidationError

class SecretForm(FlaskForm):
    title = StringField('Title',validators=[Required()])
    post = TextAreaField('Secret', validators=[Required()])
    submit = SubmitField('Submit')
 
    
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
    
