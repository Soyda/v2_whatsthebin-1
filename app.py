#the new things
import os
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, url_for
from flask_dance.contrib.google import make_google_blueprint, google
#ça finit ici
import logging
from project import app

load_dotenv()
app= Flask(__name__)
client_id = os.getenv('GOOGLE_CLIENT_ID')
client_secret = os.getenv('GOOGLE_CLIENT_SECRET')
app.secret_key=os.getenv('secret_key')

if __name__ == "__main__":
    app.run(debug=True)