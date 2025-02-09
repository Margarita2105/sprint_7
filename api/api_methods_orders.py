import requests
import curl
import allure

class ApiMethodsOrder:

    @staticmethod
    @allure.step('Создаем новый заказ.')
    def order_new(firstName_new: str, lastName_new: str, address_new: str, metroStation_new: int, phone_new: str, rentTime_new: int, deliveryDate_new: str, comment_new: str, color_new: str):
        return requests.post(curl.orders_api, json={"firstName": firstName_new,
        "lastName": lastName_new,
        "address": address_new,
        "metroStation": metroStation_new,
        "phone": phone_new,
        "rentTime": rentTime_new,
        "deliveryDate": deliveryDate_new,
        "comment": comment_new,
        "color": [color_new]
        })

    @staticmethod
    @allure.step('Получаем список заказов.')
    def order_list():
        return requests.get(curl.orders_api)

    @staticmethod
    @allure.step('Отменяем заказ.')
    def order_cancel(track_order):
        return requests.put(curl.orders_api_cancel, json={"track": track_order})
