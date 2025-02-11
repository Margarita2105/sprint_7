from api.api_methods_courier import ApiMethods
import allure
from api.data import Response
from api.helpers import generate_random_string, data
import pytest

class TestCourierNew:
    @allure.step('Создаем нового курьера, проверяем ответ сервера.')
    def test_courier(self, login):
        login_courier = login[0]
        password_courier = login[1]
        first_name_courier = login[2]
        response = ApiMethods.courier_new(login_courier, password_courier, first_name_courier)
        assert response.json() == {'ok': True} and response.status_code == 201

    @allure.step('Проверяем невозможность создать двух одинаковых курьеров.')
    def test_courier_two(self, login):
        login_courier = login[0]
        password_courier = login[1]
        first_name_courier= login[2]
        ApiMethods.courier_new(login_courier, password_courier, first_name_courier)
        response = ApiMethods.courier_new(login_courier, password_courier, first_name_courier)
        assert response.json() == Response.code_409_new_courier and response.status_code == 409

    @allure.step('Проверяем невозможность создать курьера без логина и без пароля.')
    @pytest.mark.parametrize("login_courier, password_courier", [('', data), (data, '')])
    def test_no_login_field_courier_password(self, login_courier, password_courier):
        login_courier = login_courier
        password_courier = password_courier
        first_name_courier = generate_random_string(10)
        response = ApiMethods.courier_new(login_courier, password_courier, first_name_courier)
        assert response.json() == Response.code_400_new_courier and response.status_code == 400