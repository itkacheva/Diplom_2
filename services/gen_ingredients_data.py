from random import randint

from endpoints.ingredients_endpoints import IngredientAPI


def gen_ingredients_data():
    i = IngredientAPI()
    dict_ingr = i.get_list_id_ingredient()
    selected_id = []

    # случайные id, случайное кол-во раз
    for i in range(1, randint(1, len(dict_ingr))):
        index = randint(0, len(dict_ingr) - 1)
        selected_id.append(dict_ingr[index])
        dict_ingr.remove(dict_ingr[index])

    return ({"ingredients": selected_id})
