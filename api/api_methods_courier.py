import requests
import curl
import allure

class ApiMethods:

    @staticmethod
    @allure.step('Создаем курьера.')
    def courier_new(login_new: str, password_new: str, first_name_new : str):
        return requests.post(curl.courier_api, json={"login": login_new, "password": password_new, "firstName": first_name_new })

    @staticmethod
    @allure.step('Авторизуемся под созданным логином куьера.')
    def login_courier(login_courier: str, password_courier: str):
        return requests.post(curl.login_courier_api, json={"login": login_courier, "password": password_courier})

    @staticmethod
    @allure.step('Удаляем созданного курьера после прохождения теста.')
    def courier_delete(login_delete: str, password_delete: str):
        id_response = requests.post(curl.login_courier_api, json={"login": str(login_delete), "password": str(password_delete)})
        id_delete = id_response.json()['id']
        return requests.delete(curl.courier_api+'/'+str(id_delete))
