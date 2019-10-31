from flask import render_template,redirect,url_for,request,abort
from . import main

@main.route('/')
def index():
    title = 'Home'


    return render_template('index.html')

    #Tested upvote function 

# @main.route('/upvote/<int:id>',methods=['GET','POST'])

# def upvote(id):
#     posts=post.query.get_or_404(id)
#     if request.args.get("like"):
#         postes.like = posts.like+1

#         db.session.add(posts)
#         db.session.commit()

#         return redirect("/upvote/{post_id}".format(post_id=posts.id))


#     title= 'Likes'
#     return render_template('/index.html',posts=posts, title = title )


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