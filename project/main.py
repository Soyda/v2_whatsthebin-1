from crypt import methods
from flask import Blueprint, render_template, redirect,url_for

from project import auth
from flask_login import login_required,current_user
from . import db

main = Blueprint('main', __name__)

# @auth.route('/signup')
# def signup():
#     return render_template('signup.html')

# @auth.route('/signup',methods=['POST'])
# def signup_post():
#     return redirect(url_for('auth.login'))
@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html',name=current_user.name)