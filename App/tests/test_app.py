from codecs import ascii_encode
from unicodedata import name
from urllib import response
from ..models import User
from .. import app
from werkzeug.security import generate_password_hash, check_password_hash
import pytest


def test_new_user():
    user = User(email="mailmail.com", password="1234", name="Jesuisuntest")
    assert user.email == "mailmail.com"
    assert user.password == "1234"
    assert user.name == "Jesuisuntest"

def test_home_page():
    with app.test_client() as test_client:
        response = test_client.get("/")
        assert response.status_code == 200
