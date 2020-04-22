from flask_uploads import UploadSet, IMAGES
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import TextAreaField
from wtforms.validators import DataRequired, Email,Required


images = UploadSet('images', IMAGES)

class UploadForm(FlaskForm):
    description = TextAreaField('Message', validators=[DataRequired()])
    photo = FileField('image', validators=[
        FileRequired(),
        FileAllowed(images, 'Images only!')
    ])
