import requests
import curl
import allure

class ApiMethodsOrder:

    @staticmethod
    @allure.step('Создаем новый заказ.')
    def order_new(firstName: str, lastName: str, address: str, metroStation: int, phone: str, rentTime: int, deliveryDate: str, comment: str, color: str):
        return requests.post(curl.orders_api, json={"firstName": firstName,
        "lastName": lastName,
        "address": address,
        "metroStation": metroStation,
        "phone": phone,
        "rentTime": rentTime,
        "deliveryDate": deliveryDate,
        "comment": comment,
        "color": [color]
        })

    @staticmethod
    @allure.step('Получаем список заказов.')
    def order_list():
        return requests.get(curl.orders_api)
