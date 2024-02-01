from faker import Faker

fake = Faker()


def generate_test_email():
    return fake.email()
