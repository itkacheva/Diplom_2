import requests
from urls import Urls


class IngredientAPI:

    def get_list_id_ingredient(self):
        response = requests.get(Urls.service_url + Urls.get_ingredients)
        list_ingredients = []
        for i in response.json()["data"]:
            list_ingredients.append(i['_id'])
        return list_ingredients
