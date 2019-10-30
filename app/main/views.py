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
# @login_required
def new_post():
    form= SecretForm()
    
    # if form.validate_on_submit():
        # post = Post(title = form.title.data,content = form.content.data, author=current_user)
        
    # flash('Post created', 'success')
    # return redirect(url_for('main.home'))
    return render_template('new_secret.html',title='New post', form=form)