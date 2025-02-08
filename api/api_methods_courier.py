import requests
import curl
import allure

class ApiMethods:

    @staticmethod
    @allure.step('Создаем курьера.')
    def courier_new(login: str, password: str, firstName: str):
        return requests.post(curl.courier_api, json={"login": login, "password": password, "firstName": firstName})

    @staticmethod
    @allure.step('Авторизуемся под созданным логином куьера.')
    def login_courier(login: str, password: str):
        return requests.post(curl.login_courier_api, json={"login": login, "password": password})

    @staticmethod
    @allure.step('Удаляем созданного курьера после прохождения теста.')
    def courier_delete(login: str, password: str):
        id_response = requests.post(curl.login_courier_api, json={"login": str(login), "password": str(password)})
        id = id_response.json()['id']
        return requests.delete(curl.courier_api+'/'+str(id))
