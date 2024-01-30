import requests
from urls import Urls


class UserAPI:

    def create_user(self, user_data):
        response = requests.post(Urls.service_url + Urls.create_user_url, data=user_data)
        return response

    def delete_user_by_username(self, user_data):
        response_login = self.login_user(user_data)
        headers = {
            'Authorization': response_login.json()["accessToken"]
        }
        response = requests.delete(Urls.service_url + Urls.delete_user_url, headers=headers)
        return response

    def delete_user_by_token(self, token):
        headers = {
            'Authorization': token
        }
        response = requests.delete(Urls.service_url + Urls.delete_user_url, headers=headers)
        return response

    def login_user(self, user_data):
        response = requests.post(Urls.service_url + Urls.login_user_url, data=user_data)
        return response

    def change_data_user_with_authorization(self, user_data, new_user_data):
        response_login = self.login_user(user_data)
        headers = {
            'Authorization': response_login.json()["accessToken"]
        }
        data = {
                "email": new_user_data["email"],
                "name": new_user_data["name"]
            }
        response = requests.patch(Urls.service_url + Urls.change_data_user_url, data=data, headers=headers)
        return response

    def change_data_user_without_authorization(self, new_user_data):
        data = {
                "email": new_user_data["email"],
                "name": new_user_data["name"]
            }
        response = requests.patch(Urls.service_url + Urls.change_data_user_url, data=data)
        return response
