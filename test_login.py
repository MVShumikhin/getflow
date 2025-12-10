import requests
import pytest

@pytest.mark.parametrize('email,password',[
    ("rrrttttr@mail.ru","rrrrrr"),
    ('tttttt@mail.ru','ttttttt')
])
def test_login_status(email,password):
    url = "http://2.59.41.2:7320/api/auth/login"
    pay = {
        "email":email,
        "password": password
    }
    response = requests.post(url,json=pay)
    assert response.status_code == 401

