import string
import random

import pytest

import data
from burger_api import UserApi as user_api, OrderApi as order_api
from helper import delete_data_field


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


@pytest.fixture(scope='function')
def generate_registration_data():
    email = f'{generate_random_string(10)}@yandex.ru'
    password = generate_random_string(10)
    name = generate_random_string(10)

    data = {
        "email": email,
        "password": password,
        "name": name
    }
    return data


def create_and_login_user():
    user_data = generate_registration_data
    response = user_api.create_user(user_data)
    json_response = response.json()
    token = json_response['accessToken']
    login_data = delete_data_field(user_data, 'name')
    login_response = user_api.login_user(login_data)
    order_response = order_api.create_order(data.BurgerIngredientsData)
    assert order_response.status_code == 200

    assert login_response.status_code == 200
    assert user_api.delete_user(token).status_code == 202
