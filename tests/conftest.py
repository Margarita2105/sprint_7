import pytest
from api.helpers import generate_random_string
from api.helpers import register_new_courier_and_return_login_password
from api.api_methods_courier import ApiMethods

@pytest.fixture
def login():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    login_pass = [login, password, first_name]

    yield login_pass
    ApiMethods.courier_delete(login, password)

@pytest.fixture
def login_generate():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    login_pass = [login, password, first_name]

    return login_pass

@pytest.fixture
def register():
    register = register_new_courier_and_return_login_password()
    yield register
    ApiMethods.courier_delete(register[0], register[1])
