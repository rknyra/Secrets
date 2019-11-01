from . import db,login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    
    __tablename__ = 'users'
    
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    password_hash=db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String(), default='profpic.png')
    posts =  db.relationship('Post', backref = 'user', lazy = "dynamic")
    comments = db.relationship('Comment', backref = 'user', lazy = "dynamic")
   
    
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)
    

    def __repr__(self):
        return f'User {self.username}'
    
    
class Category(db.Model):
    
    __tablename__= 'categories'
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255), index = True)
    

    @classmethod
    def get_categories(cls):
        categories = Category.query.all()
        return categories
    
    
class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255), index = True)
    post = db.Column(db.String(300), index = True)
    time = db.Column(db.DateTime, default = datetime.utcnow)
    upvote = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    comments = db.relationship('Comment', backref = 'post', lazy = "dynamic")

    def save_post(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_posts(cls, id):
        posts = Post.query.filter_by(category_id = id).all()
        return posts
    
    @classmethod
    def get_posts_user(cls,id):
        posts = Post.query.filter_by(user_id = id).all()
        return posts
    
    
class Comment(db.Model):
    
    __tablename__ = 'comments'
    
    id = db.Column(db.Integer, primary_key = True)
    comment_post = db.Column(db.String(255), index=True)
    time = db.Column(db.DateTime, default=datetime.utcnow)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    def save_comments(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls, id):
        comments = Comment.query.filter_by(post_id=id).all()
        return comments