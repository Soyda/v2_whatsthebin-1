from flask import Blueprint, render_template
from flask_login import login_required, current_user
# from flask_security import roles_required
from . import db, app
import os

 # for monitoring with azure insights
from applicationinsights.flask.ext import AppInsights
from logging import StreamHandler, Formatter, DEBUG

app.config['APPINSIGHTS_INSTRUMENTATIONKEY'] = 'e72fcfed-d1af-4e45-ba8a-5dd76ab76920'
appinsights = AppInsights(app)

# keep stdout/stderr logging using StreamHandler
streamHandler = StreamHandler()
app.logger.addHandler(streamHandler)

# define log level to DEBUG
app.logger.setLevel(DEBUG)

# apply same formatter on all log handlers
for logHandler in app.logger.handlers:
  logHandler.setFormatter(Formatter('[FLASK-SAMPLE][%(levelname)s]%(message)s'))

main = Blueprint('main', __name__)

# for monitoring with azure insights
# force flushing application insights handler after each request
@app.after_request
def after_request(response):
    appinsights.flush()
    return response


@main.route('/')
def index():
    # testing monitoring log messages
    app.logger.debug('This is a debug log message')
    app.logger.info('This is an information log message')
    app.logger.warn('This is a warning log message')
    app.logger.error('This is an error message')
    app.logger.critical('This is a critical message')

    # remove image files from root
    for file in os.listdir() :
        if file.endswith(('.png', ".jpg", ".jpeg", ".webp", ".JPG", ".JPEG")):
            os.remove(file) 

    return render_template("index.html")

@main.route('/profile')
@login_required
def profile():
    return render_template("profile.html", name=current_user.name)


# TEST WITH ROLES
# @main.route("/admin")
# @roles_required('Admin')
# def admin_page():
#     return "If you're here this means you're an admin user"

# @main.route("/standard")
# @roles_required('Standard')
# def admin_page():
#     return "If you're here this means you're a standard user"


