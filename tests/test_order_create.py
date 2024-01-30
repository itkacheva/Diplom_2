import allure

from endpoints.order_endpoints import OrderAPI
from services.gen_ingredients_data import *


class TestOrderCreate:
    @allure.title('Проверяем создание заказа без авторизации c ингридиентами.')
    @allure.description('Создаем заказ проверяем статус и текст ответа')
    def test_order_create_without_authorization_success(self):
        response = OrderAPI().create_order_without_authorization(gen_ingredients_data())
        assert response.status_code == 200 and response.json()["order"]["number"]

    @allure.title('Проверяем создание заказа без авторизации без ингридиентов.')
    @allure.description('Создаем заказ проверяем статус и текст ответа')
    def test_order_create_without_authorization_fail(self):
        response = OrderAPI().create_order_without_authorization({"ingredients": []})
        assert response.status_code == 400 and response.json()["message"] == "Ingredient ids must be provided"

    @allure.title('Проверяем создание заказа без авторизации c неверным хешем ингридиентов.')
    @allure.description('Создаем заказ проверяем статус и текст ответа')
    def test_order_create_without_authorization_bad_hash_fail(self):
        response = OrderAPI().create_order_without_authorization({"ingredients": ["111111171d1f82001bdaaa6d"]})
        assert response.status_code == 400 and response.json()["message"] == "One or more ids provided are incorrect"

    @allure.title('Проверяем создание заказа с авторизацией c ингридиентами.')
    @allure.description('Создаем заказ проверяем статус и текст ответа')
    def test_order_create_with_authorization_success(self, user):
        response = OrderAPI().create_order_with_authorization(gen_ingredients_data(), user)
        assert response.status_code == 200 and response.json()["order"]["number"]

    @allure.title('Проверяем создание заказа с авторизацией без ингридиентов.')
    @allure.description('Создаем заказ проверяем статус и текст ответа')
    def test_order_create_with_authorization_fail(self, user):
        response = OrderAPI().create_order_with_authorization({"ingredients": []}, user)
        assert response.status_code == 400 and response.json()["message"] == "Ingredient ids must be provided"

    @allure.title('Проверяем создание заказа с авторизацией c неверным хешем ингридиентов.')
    @allure.description('Создаем заказ проверяем статус и текст ответа')
    def test_order_create_with_authorization_bad_hash_fail(self, user):
        response = OrderAPI().create_order_with_authorization({"ingredients": ["122111171d1f82001bdaaa6d"]}, user)
        assert response.status_code == 400 and response.json()["message"] == "One or more ids provided are incorrect"