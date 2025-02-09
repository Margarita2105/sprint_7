from api.api_methods_courier import ApiMethods
import allure
from api.data import Response

class TestCourierLogin:

    @allure.step('Авторизуемся под существующим логином курьера, получаем его id и ответ сервера.')
    def test_courier_login(self, register):
        login_courier = register[0]
        password = register[1]
        response = ApiMethods.login_courier(login_courier, password)
        courier_id = response.json()['id']
        assert response.json() == {'id': courier_id} and response.status_code == 200

    @allure.step('Проверяем невозможность авторизоваться не передавая логин курьера.')
    def test_no_login_field_courier_login(self, register):
        login_courier = ''
        password = register[1]
        response = ApiMethods.login_courier(login_courier, password)
        assert response.json() == Response.code_400_login_courier and response.status_code == 400

    @allure.step('Проверяем невозможность авторизоваться не передавая пароль от логина курьера.')
    def test_no_password_field_courier_login(self, register):
        login_courier = register[0]
        password = ''
        response = ApiMethods.login_courier(login_courier, password)
        assert response.json() == Response.code_400_login_courier and response.status_code == 400

    @allure.step('Проверяем невозможность авторизоваться передав некорректный логин курьера.')
    def test_incorrect_login_courier_login(self, register):
        login_courier = 'логин'
        password = register[1]
        response = ApiMethods.login_courier(login_courier, password)
        assert response.json() == Response.code_404_login_courier and response.status_code == 404

    @allure.step('Проверяем невозможность авторизоваться передав некорректный пароль от логина курьера.')
    def test_incorrect_password_courier_login(self, register):
        login_courier = register[0]
        password = '123'
        response = ApiMethods.login_courier(login_courier, password)
        assert response.json() == Response.code_404_login_courier and response.status_code == 404
