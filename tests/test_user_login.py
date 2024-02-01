import allure

from endpoints.user_endpoints import UserAPI


class TestUserLogin:

    @allure.title('Проверяем вход под существующим пользователем.')
    @allure.description('Создаем пользователя, осуществляем вход и проверяем статус и текст ответа')
    def test_user_login_exist_user_success(self, user):
        response = UserAPI().login_user(user)
        assert response.status_code == 200 and response.json()["success"] == True

    @allure.title('Проверяем вход под существующим пользователем.Указываем не верный логин')
    @allure.description('Создаем пользователя, осуществляем вход с неверным логином и проверяем статус и текст ответа')
    def test_user_login_bad_login_fail(self, user):
        response = UserAPI().login_user({"email": "fail_email", "password": user["password"]})
        assert response.status_code == 401 and response.json()["message"] == "email or password are incorrect"

    @allure.title('Проверяем вход под существующим пользователем.Указываем не верный пароль')
    @allure.description('Создаем пользователя, осуществляем вход с неверным паролем и проверяем статус и текст ответа')
    def test_user_login_bad_password_fail(self, user):
        response = UserAPI().login_user({"email": user["email"], "password": "fail_password"})
        assert response.status_code == 401 and response.json()["message"] == "email or password are incorrect"
