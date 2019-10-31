
from flask import render_template,redirect,url_for,request,abort
from . import main



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

