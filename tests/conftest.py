import pytest
import random
import string
from api.new_login import register_new_courier_and_return_login_password


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

@pytest.fixture
def login():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    login_pass = []
    login_pass.append(login)
    login_pass.append(password)
    login_pass.append(first_name)
    return login_pass

@pytest.fixture
def register():
    return register_new_courier_and_return_login_password()