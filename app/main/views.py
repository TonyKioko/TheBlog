from flask import render_template,request,redirect,url_for, abort
from . import main
from flask_login import login_required,current_user
from .forms import PostsForm,CommentsForm,UpdateProfile
from ..models import Posts,Comments,User
from .. import photos, db
from datetime import datetime

@main.route('/')
# @login_required
def home():

    '''
    View root page function that returns the general news sources by category
    '''
    # message = "Hello World"
    title="Pitches"
   
    

    message= 'Welcome to the Blog'
    # return "Hello, World"
    return render_template('home.html',title=title,message=message)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)
@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/post/new',methods = ['GET','POST'])
@login_required
def new_pitch():
    '''
    View pitch function that returns the pitch page and data
    '''
    form = PostsForm()

    if form.validate_on_submit() and form.category.data != 'Select':
        body = form.body.data
        category = form.category.data

        new_post = Posts(body=body,category=category,user_id=current_user.id)
        new_post.save_post()

        return redirect(url_for('main.home'))

    return render_template('new_post.html', pitch_form = form)
