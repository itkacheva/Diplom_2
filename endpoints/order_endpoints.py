import requests

from endpoints.user_endpoints import UserAPI
from urls import Urls


class OrderAPI:

    def create_order_without_authorization(self, order_data):
        response = requests.post(Urls.service_url + Urls.create_order_url, data=order_data)
        return response

    def create_order_with_authorization(self, order_data, user_data):
        response_login = UserAPI().login_user(user_data)
        headers = {
            'Authorization': response_login.json()["accessToken"]
        }
        response = requests.post(Urls.service_url + Urls.create_order_url, data=order_data, headers=headers)
        return response

    def get_data_order_by_user_name_with_authorization(self, user_data):
        response_login = UserAPI().login_user(user_data)
        headers = {
            'Authorization': response_login.json()["accessToken"]
        }
        response = requests.get(Urls.service_url + Urls.get_data_order_url, headers=headers)
        return response

    def get_data_order_by_user_name_without_authorization(self):
        response = requests.get(Urls.service_url + Urls.get_data_order_url)
        return response
