from flask import render_template
from . import auth
from flask import render_template,redirect,url_for, flash,request
from flask_login import login_user,logout_user,login_required
from app.models import User
from .forms import RegistrationForm,LoginForm
from .. import db
from ..email import mail_message