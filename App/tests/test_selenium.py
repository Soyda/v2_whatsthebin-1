from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

import os, sys, inspect
from .. import app
from .. import models
from ..models import User

# Third party modules
import pytest

# First party modules
from flask import Flask


@pytest.fixture
def client():
    app = Flask(__name__)
    # app.config.from_object('main.tests.config')
    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    # A partir de celui-ci je déduis le chemin de mon répertoire parent
    # parentdir = os.path.dirname(currentdir)
    # grandparentdir = os.path.dirname(parentdir)
    template_folder_path = "../templates" #os.path.join(grandparentdir, "/tests/templates")
    app.template_folder = template_folder_path
    db = SQLAlchemy(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
    # since the id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(id))


    # blueprint for auth routes in our app
    from ..auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, template_folder = template_folder_path)

    # blueprint for non-auth parts of app
    from ..main import main as main_blueprint
    app.register_blueprint(main_blueprint, template_folder = template_folder_path)

    client = app.test_client()

    with app.app_context():
        # init_db()
        db.drop_all()
        db.create_all()
        
        # first_user = User(
        #     id = 1,
        #     email = "cb@gmail.com",
        #     password = 'sha256$zU9nb9Fu6i2pLdmP$a1587105ab6efe3dd726cade3e95ab3ac039d58c0ecf40395871a0a071948c8f',
        #     name = "Charles",
        #     group = 0 # 0 mean admin
        #     )
        # first_user.save_to_db()
        
        # second_user = User(
        #     id = 2,
        #     email = "tv@gmail.com",
        #     password = 'sha256$zU9nb9Fu6i2pLdmP$a1587105ab6efe3dd726cade3e95ab3ac039d58c0ecf40395871a0a071948c8f',
        #     name = "Tony",
        #     group = 1 # 1 mean user
        #     )
        # second_user.save_to_db()

        
    yield client

@pytest.fixture
def driver():
    chrome_driver = "./chromedriver"
    with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as driver:
        yield driver


def test_get_index(client):
    route = "/"
    rv = client.get(route)
    assert rv.status_code == 200
    assert b"Easy authentication and authorization in Flask." in rv.data
    assert b"Flask Login Example" in rv.data

def test_post_index(client):
    route = "/"
    rv = client.post(route)
    assert rv.status_code == 405
    assert b"Flask Login Example" not in rv.data

# from flask import session

# def test_access_session(client):
#     with client:
#         client.post("/login", data={"email": "stevendruesne@gmail.com", "password": "1234"})
#         # session is still accessible
#         assert session["user_name"] == "steven"

#     # session is no longer accessible
