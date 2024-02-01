import allure

from endpoints.user_endpoints import UserAPI
from services.gen_user_data import *


class TestUserCreate:

    @allure.title('Проверяем, что можно создать уникального пользователя.')
    @allure.description('Создаем пользователя, проверяем статус и текст ответа')
    def test_user_create_unique_successfull(self):
        user_data = gen_user_data()
        u = UserAPI()
        response = u.create_user(user_data)
        u.delete_user_by_username(user_data)
        assert response.status_code == 200 and response.json()["success"]==True

    @allure.title('Проверяем, что нельзя создать двух одинаковых пользователей.')
    @allure.description('Создаем пользователя повторно, проверяем статус ответа и сообщение')
    def test_user_two_identical_users_status_code_403(self, user):
        response = UserAPI().create_user(user)
        assert response.status_code == 403 and\
                   response.json()["message"] == 'User already exists'

    @allure.title('Проверяем, что если нет обязательного поля "email", запрос возвращает ошибку.')
    @allure.description('Создаем пользователя, не передав обязательное поле и проверяем текст ошибки')
    def test_user_create_without_email_error_message(self):
        user_data = gen_user_data()
        response = UserAPI().create_user({"password": user_data["password"], "name": user_data["name"]})
        r = response.json()
        assert response.status_code == 403 and \
               r["message"] == 'Email, password and name are required fields'

    @allure.title('Проверяем, что если нет обязательного поля "password", запрос возвращает ошибку.')
    @allure.description('Создаем пользователя, не передав обязательное поле и проверяем текст ошибки')
    def test_user_create_without_password_error_message(self):
        user_data = gen_user_data()
        response = UserAPI().create_user({"email": user_data["email"], "name": user_data["name"]})
        r = response.json()
        assert response.status_code == 403 and \
               r["message"] == 'Email, password and name are required fields'

    @allure.title('Проверяем, что если нет обязательного поля "name", запрос возвращает ошибку.')
    @allure.description('Создаем пользователя, не передав обязательное поле и проверяем текст ошибки')
    def test_user_create_without_name_error_message(self):
        user_data = gen_user_data()
        response = UserAPI().create_user({"email": user_data["email"], "password": user_data["password"]})
        r = response.json()
        assert response.status_code == 403 and \
               r["message"] == 'Email, password and name are required fields'