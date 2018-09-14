from flask import render_template,request,redirect,url_for, abort
from . import main
from flask_login import login_required,current_user
from .forms import PitchesForm,CommentsForm,UpdateProfile
from ..models import Posts,Comments,User
from .. import photos, db
from datetime import datetime

@main.route('/')
def home():

    '''
    View root page function that returns the general news sources by category
    '''
    # message = "Hello World"
    title="Pitches"
   
    

    message= 'Welcome to the Blog'
    # return "Hello, World"
    return render_template('home.html',title=title,message=message)