import pytest

from endpoints.user_endpoints import UserAPI
from services.gen_user_data import gen_user_data


@pytest.fixture(scope="function")
def user():
    user_data = gen_user_data()
    UserAPI().create_user(user_data)

    yield user_data
    UserAPI().delete_user_by_username(user_data)
