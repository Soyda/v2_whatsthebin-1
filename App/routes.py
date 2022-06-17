from App import app
from flask import render_template


def compute_item():
    compute = 2 * 2 
    return compute 


@app.route('/')
def homepage():
    chiffre = compute_item()
    return render_template("home.html", chiffre=chiffre)