# from App import app
# from flask import render_template


# def compute_item():
#     compute = 2 * 2 
#     return compute 


# @app.route('/')
# def homepage():
#     chiffre = compute_item()
#     return render_template("home.html", chiffre=chiffre)

from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template("index.html")

@main.route('/profile')
@login_required
def profile():
    return render_template("profile.html", name=current_user.name)