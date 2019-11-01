from flask import render_template,redirect,url_for,request,abort,flash
from . import main
from ..models import User, Post, Comment,Category
from .forms import SecretForm, UpdateProfile
from flask_login import login_required, current_user
from .. import db, photos



@main.route('/')
def index():
    return render_template('index.html')


@main.route('/home')
@login_required
def home():
    
    categories = Category.get_categories()
    title = 'posts'
    print(categories)
    return render_template('home_page.html',categories=categories,title=title)


@main.route('/categories/<int:id>')
def post_types(id):
    category = Category.query.get(id)
    title = f'{category.name} posts'
    posts = Post.get_posts(category.id)
    
    return render_template('secrets.html',title=title,category=category,posts=posts,user=current_user)

@main.route("/post")
def post():
    return render_template('secrets.html')


@main.route('/category/post/new/<int:id>', methods=["GET", "POST"])
@login_required
def post_new(id):
    '''
    view function that helps renders the form to create a new post
    '''
    form = SecretForm()
    categories = Category.query.filter_by(id=id).first()
    if form.validate_on_submit():
        post = form.post.data
        title = form.title.data
        new_post = Post(category_id=categories.id, title=title, post=post, user=current_user)
        new_post.save_post()
        return redirect(url_for('.post_types', id=categories.id))
    
    title = f'{categories.name} posts'
    return render_template('new_secret.html', title=title, post_form=form, categories=categories)

@main.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):

    post = Post.query.get_or_404(post_id)
    
    if post.user != current_user:
        abort(403)
    form = SecretForm()
    categories = Category.query.filter_by(id=post_id).first()
    if form.validate_on_submit():
        post.title = form.title.data
        post.post = form.post.data
        new_post = Post(category_id=categories.id, title=post.title, post=post.post, user=current_user)
        new_post.save_post()
        
        print(post)
        flash('Post updated!', 'success')
        return redirect(url_for('.post_types',id=categories.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.post.data = post.post
    return render_template('new_secret.html', title='Update Post',
                           form=form, legend='Update Post', post_form=form,categories=categories)
    
    
@main.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    
    post = Post.query.get(post_id)
    if post.user != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Post deleted!', 'success')
    return redirect(url_for('main.home'))


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
    posts=Post.query.get_or_404(id)
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