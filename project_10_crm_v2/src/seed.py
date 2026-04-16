from faker import Faker
from user import User


def seed(n: int = 10):
    """ Seed the database with fake users.

    Args:
        n (int, optional): The number of fake users to create. Defaults to 10.
    """
    fake = Faker(locale="fr_FR")
    for _ in range(n):
        user = User(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            phone_number=fake.phone_number(),
            adress=fake.address()
        )
        user.save()


if __name__ == "__main__":
    seed(2)
