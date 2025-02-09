from api.api_methods_courier import ApiMethods
import allure
from api.data import Response

class TestCourierNew:
    @allure.step('Создаем нового курьера, проверяем ответ сервера.')
    def test_courier(self, login):
        login_courier = login[0]
        password_courier = login[1]
        firstName_courier = login[2]
        response = ApiMethods.courier_new(login_courier, password_courier, firstName_courier)
        assert response.json() == {'ok': True} and response.status_code == 201

    @allure.step('Проверяем невозможность создать двух одинаковых курьеров.')
    def test_courier_two(self, login):
        login_courier = login[0]
        password_courier = login[1]
        firstName_courier= login[2]
        ApiMethods.courier_new(login_courier, password_courier, firstName_courier)
        response = ApiMethods.courier_new(login_courier, password_courier, firstName_courier)
        assert response.json() == Response.code_409_new_courier and response.status_code == 409

    @allure.step('Проверяем невозможность создать курьера без логина.')
    def test_no_login_field_courier(self, login_generate):
        login_courier = ''
        password_courier = login_generate[1]
        firstName_courier = login_generate[2]
        response = ApiMethods.courier_new(login_courier, password_courier, firstName_courier)
        assert response.json() == Response.code_400_new_courier and response.status_code == 400

    @allure.step('Проверяем невозможность создать курьера без пароля')
    def test_no_password_field_courier(self, login_generate):
        login_courier = login_generate[0]
        password_courier = ''
        firstName_courier = login_generate[2]
        response = ApiMethods.courier_new(login_courier, password_courier, firstName_courier)
        assert response.json() == Response.code_400_new_courier and response.status_code == 400
