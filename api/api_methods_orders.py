import requests
import curl
import allure

class ApiMethodsOrder:

    @staticmethod
    @allure.step('Создаем новый заказ.')
    def order_new(first_name_new : str, last_name_new: str, address_new: str, metro_station_new: int, phone_new: str, rent_time_new: int, delivery_date_new: str, comment_new: str, color_new: str):
        return requests.post(curl.orders_api, json={"firstName": first_name_new ,
        "lastName": last_name_new,
        "address": address_new,
        "metroStation": metro_station_new,
        "phone": phone_new,
        "rentTime": rent_time_new,
        "deliveryDate": delivery_date_new,
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
