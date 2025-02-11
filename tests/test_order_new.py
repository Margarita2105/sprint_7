from api.api_methods_orders import ApiMethodsOrder
from api.data import Credential
import pytest
import allure
from api.helpers import generate_random_string

class TestOrder:

    @allure.step('Проверяем возможность создания заказа передав в заказе цвет самоката черный, серый , оба цвета, не передав цвет.')
    @pytest.mark.parametrize("color", [Credential.color_black, Credential.color_grey, Credential.color_black_grey, Credential.color_0])
    def test_order_new(self, color):
        response = ApiMethodsOrder.order_new(generate_random_string(10), generate_random_string(10), Credential.address, Credential.metro_station, Credential.phone, Credential.delivery_date, Credential.rent_time, Credential.comment, color)
        assert 'track' in response.json() and response.status_code == 201
        track_order = response.json()['track']
        ApiMethodsOrder.order_cancel(track_order)

    @allure.step('Получаем список заказов.')
    def test_list_order(self):
        response = ApiMethodsOrder.order_list()
        assert 'orders' in response.json() and response.status_code == 200
