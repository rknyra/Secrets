from flask import render_template
from . import main
from .forms import SecretForm

@main.route('/home')
def home():
    return render_template('home_page.html')

@main.route("/post")
def post():
    return render_template('secret.html')

@main.route("/post/new", methods=['GET','POST'])
def new_post():
    form= SecretForm()
    return render_template('new_secret.html',title='New post', form=form)