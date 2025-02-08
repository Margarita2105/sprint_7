from api.api_methods_courier import ApiMethods
import allure

class TestCourierNew:
    @allure.step('Создаем нового курьера, проверяем ответ сервера.')
    def test_courier(self, login):
        login_courier = login[0]
        password = login[1]
        firstName = login[2]
        response = ApiMethods.courier_new(login_courier, password, firstName)
        assert response.json() == {'ok': True} and response.status_code == 201
        ApiMethods.courier_delete(login_courier, password)

    @allure.step('Проверяем невозможность создать двух одинаковых курьеров.')
    def test_courier_two(self, login):
        login_courier = login[0]
        password = login[1]
        firstName = login[2]
        ApiMethods.courier_new(login_courier, password, firstName)
        response = ApiMethods.courier_new(login_courier, password, firstName)
        assert response.json() == {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'} and response.status_code == 409
        ApiMethods.courier_delete(login_courier, password)

    @allure.step('Проверяем невозможность создать курьера без логина.')
    def test_no_login_field_courier(self, login):
        login_courier = ''
        password = login[1]
        firstName = login[2]
        response = ApiMethods.courier_new(login_courier, password, firstName)
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'} and response.status_code == 400

    @allure.step('Проверяем невозможность создать курьера без пароля')
    def test_no_password_field_courier(self, login):
        login_courier = login[0]
        password = ''
        firstName = login[2]
        response = ApiMethods.courier_new(login_courier, password, firstName)
        assert response.json() == {'code': 400,
                                   'message': 'Недостаточно данных для создания учетной записи'} and response.status_code == 400
