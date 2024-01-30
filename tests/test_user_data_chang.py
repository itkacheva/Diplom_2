import allure

from endpoints.user_endpoints import UserAPI


class TestUserDataChange:

    @allure.title('Проверяем изменение данных пользователя с авторизацией. Меняем имя.')
    @allure.description('Создаем пользователя, меняем имя и проверяем статус и текст ответа')
    def test_user_change_data_set_new_name_success(self, user):
        user_new = user.copy()
        user_new["name"] += "_new"
        response = UserAPI().change_data_user_with_authorization(user, user_new)
        UserAPI().change_data_user_with_authorization(user_new, user)
        assert response.status_code == 200 and response.json()["user"]['name'] == user_new["name"]

    @allure.title('Проверяем изменение данных пользователя с авторизацией. Меняем email.')
    @allure.description('Создаем пользователя, меняем email и проверяем статус и текст ответа')
    def test_user_change_data_set_new_email_success(self, user):
        user_new = user.copy()
        user_new["email"] += "_new"
        response = UserAPI().change_data_user_with_authorization(user, user_new)
        UserAPI().change_data_user_with_authorization(user_new, user)
        assert response.status_code == 200 and response.json()["user"]['email'].upper() == user_new["email"].upper()

    @allure.title('Проверяем изменение данных пользователя без авторизации. Меняем имя.')
    @allure.description('Создаем пользователя, меняем имя и проверяем статус и текст ответа')
    def test_user_change_data_set_new_name_fail(self, user):
        user_new = user.copy()
        user_new["name"] = user["name"]+"_new"
        response = UserAPI().change_data_user_without_authorization(user_new)
        assert response.status_code == 401 and response.json()['message'] == "You should be authorised"

    @allure.title('Проверяем изменение данных пользователя без авторизации.  Меняем email.')
    @allure.description('Создаем пользователя, меняем email и проверяем статус и текст ответа')
    def test_user_change_data_set_new_email_fail(self, user):
        user_new = user.copy()
        user_new["email"] = user["email"]+"_new"
        response = UserAPI().change_data_user_without_authorization(user_new)
        assert response.status_code == 401 and response.json()['message'] == "You should be authorised"
