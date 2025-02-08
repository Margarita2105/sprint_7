from api.api_methods_courier import ApiMethods
import allure

class TestCourierLogin:

    @allure.step('Авторизуемся под существующим логином курьера, получаем его id и ответ сервера.')
    def test_courier_login(self, register):
        login_courier = register[0]
        password = register[1]
        response = ApiMethods.login_courier(login_courier, password)
        id = response.json()['id']
        assert response.json() == {'id': id} and response.status_code == 200
        ApiMethods.courier_delete(login_courier, password)

    @allure.step('Проверяем невозможность авторизоваться не передавая логин курьера.')
    def test_no_login_field_courier_login(self, register):
        login_courier = ''
        password = register[1]
        response = ApiMethods.login_courier(login_courier, password)
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для входа'} and response.status_code == 400

    @allure.step('Проверяем невозможность авторизоваться не передавая пароль от логина курьера.')
    def test_no_password_field_courier_login(self, register):
        login_courier = register[0]
        password = ''
        response = ApiMethods.login_courier(login_courier, password)
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для входа'} and response.status_code == 400

    @allure.step('Проверяем невозможность авторизоваться передав некорректный логин курьера.')
    def test_incorrect_login_courier_login(self, register):
        login_courier = 'логин'
        password = register[1]
        response = ApiMethods.login_courier(login_courier, password)
        assert response.json() == {'code': 404,
                                   'message': 'Учетная запись не найдена'} and response.status_code == 404

    @allure.step('Проверяем невозможность авторизоваться передав некорректный пароль от логина курьера.')
    def test_incorrect_password_courier_login(self, register):
        login_courier = register[0]
        password = '123'
        response = ApiMethods.login_courier(login_courier, password)
        assert response.json() == {'code': 404,
                                   'message': 'Учетная запись не найдена'} and response.status_code == 404
