from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
                                                                                                                                        
class CreateBook(FlaskForm):
  vent = StringField('vent')