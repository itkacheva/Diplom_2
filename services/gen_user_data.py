from services.gen_fake_email import generate_test_email
from services.gen_random_string import generate_random_string


def gen_user_data():
    user_data = {"name": 'D2_3p_' + generate_random_string(10),
                 "password": 'D2_3p_' + generate_random_string(10),
                 "email": 'D2_3p_' + generate_test_email()}
    return user_data
