from flask import render_template, request,redirect,url_for,abort, flash
from . import main


@main.route('/')
def index():
    
    
    
    return render_template('index.html')


# user profile page
@main.route('/user')
def profile():
  

    title = 'Secrets: myProfile'
    return render_template("profile/profile.html", title=title)


# update profile page - update user bio
@main.route('/user/update')
# @login_required
def update_profile():
    
    
    
    
    title = 'Secrets'
    return render_template('profile/update.html', title=title)

# update prof pic
@main.route('/user/update/pic')
# @login_required
def update_pic():
    
    title = 'Secrets: myProfile'
    return render_template("profile/profile.html", title=title)
