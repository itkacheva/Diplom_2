import allure

from endpoints.order_endpoints import OrderAPI
from services.gen_ingredients_data import *


class TestOrderGet:

    @allure.title('Проверяем получение информации о заказе авторизованного пользователя.')
    @allure.description('Запрашиваем информацию изаказе, проверяем статус ответа')
    def test_order_create_with_authorization_success(self, user):
        OrderAPI().create_order_with_authorization(gen_ingredients_data(), user)
        response = OrderAPI().get_data_order_by_user_name_with_authorization(user)
        assert response.status_code == 200

    @allure.title('Проверяем получение информации о заказе не авторизованного пользователя.')
    @allure.description('Запрашиваем информацию о заказе, проверяем статус и текст ответа.')
    def test_order_create_without_authorization_fail(self):
        response = OrderAPI().get_data_order_by_user_name_without_authorization()
        assert response.status_code == 401 and response.json()["message"] == "You should be authorised"
