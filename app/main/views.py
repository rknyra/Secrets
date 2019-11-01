from flask import render_template,redirect,url_for,request,abort
from . import main
from ..models import User, Category, Post, Comment
from .forms import SecretForm, UpdateProfile
from flask_login import login_required, current_user
from .. import db, photos



@main.route('/')
def index():
    return render_template('index.html')


@main.route('/home')
@login_required
def home():
    return render_template('home_page.html')

@main.route("/post")
def post():
    return render_template('secret.html')


@main.route("/post/new", methods=['GET','POST'])
def new_post():
    form= SecretForm()

    return render_template('new_secret.html',title='New post', form=form)


# user profile page
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    title = 'Secrets: myProfile'
    return render_template("profile/profile.html", title=title, user=user)

# update profile page - update user bio
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
    
    title = 'Insights Today'
    return render_template('profile/update.html',form =form, user=user, title=title)

# update prof pic
@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))


#Tested upvote function 
@main.route('/upvote/<int:id>',methods=['GET','POST'])

def upvote(id):
    posts=post.query.get_or_404(id)
    if request.args.get("upvote"):
        postes.upvote = posts.upvote+1

        db.session.add(posts)
        db.session.commit()

        return redirect("/upvote/{post_id}".format(post_id=posts.id))


    title= 'Upvotes'
    return render_template('/index.html',posts=posts, title = title )


#The second untested upvote function- Might need Ajax

# @main.route('/vote/<int:post_id>')
# def upvote(post_id):
#     posts = models.Post.select().where(models.Post.id == post_id)
#     if posts.count() == 0:
#         abort(404)
#     post = models.Post.select().where(models.Post.id == post_id).get()
#     query = models.Post.update(upvotes = (post.upvotes+1)).where(models.Post.id == post_id)
#     query.execute()
#     return redirect(url_for('index'))

#Doesn't need ajax

# @main.route('/vote/<int:post_id>')
# def upvote(post_id):
#     posts = models.Post.select().where(models.Post.id == post_id)
#     if posts.count() == 0:
#         abort(404)
#     post = models.Post.select().where(models.Post.id == post_id).get()
#     query = models.Post.update(upvotes = (post.upvotes+1)).where(models.Post.id == post_id)
#     query.execute()
#     return redirect(url_for('index'))