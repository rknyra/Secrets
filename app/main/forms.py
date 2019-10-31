from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class SecretForm(FlaskForm):

    title = StringField('title',validators=[Required()])
    review = TextAreaField('Secret', validators=[Required()])
    submit = SubmitField('Submit')