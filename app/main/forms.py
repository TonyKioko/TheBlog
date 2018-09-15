from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SelectField,SubmitField
from wtforms.validators import Required

class PostsForm(FlaskForm):
    category = SelectField('Pitch Category',
                              choices=[('Select','Select Category'), ('Interview-Pitch', 'Interview Pitch'), ('Product-Pitch', 'Product Pitch'),
                                       ('Promotion-Pitch', 'Promotion Pitch'), ('Business-Pitch', 'Business Pitch')], validators=[Required()])
    title = StringField('Blog Title',validators = [Required()])
    body = TextAreaField('Blog Content',validators = [Required()])
    submit = SubmitField('Post')
    
class CommentsForm(FlaskForm):
    comment = TextAreaField('Comment on pitch',validators = [Required()])
    submit = SubmitField('Submit')
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')


