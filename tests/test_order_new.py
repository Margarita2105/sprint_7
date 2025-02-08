from api.api_methods_orders import ApiMethodsOrder
from api.data import Credential
import pytest
import allure

class TestOrder:

    @allure.step('Проверяем возможность создания заказа передав в заказе цвет самоката черный, серый , оба цвета, не передав цвет.')
    @pytest.mark.parametrize("color", [Credential.color_black, Credential.color_grey, Credential.color_black_grey, Credential.color_0])
    def test_order_new(self, login, color):
        response = ApiMethodsOrder.order_new(login[0], login[1], Credential.address, Credential.metroStation, Credential.phone, Credential.deliveryDate, Credential.rentTime, Credential.comment, color)
        assert 'track' in response.json() and response.status_code == 201

    @allure.step('Получаем список заказов.')
    def test_list_order(self):
        response = ApiMethodsOrder.order_list()
        assert 'orders' in response.json() and response.status_code == 200
