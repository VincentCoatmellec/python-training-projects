"""Module to generate random users"""
from faker import Faker
import logging
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
LOG_DIR = PROJECT_ROOT / "logs"
logging.basicConfig(filename=LOG_DIR / "user.log",
                    level=logging.INFO,
                    format="%(asctime)s : %(levelname)s : %(message)s")

fake = Faker()


def get_user() -> str:
    """Generate a single fake user

    Returns:
        str: user
    """
    logging.info("Generating user.")
    return f"{fake.first_name()} {fake.last_name()}"


def get_users(n: int) -> list[str]:
    """Generate n fake users

    Args:
        n (int): number of users you want to create

    Returns:
        list[str]: list of users
    """
    logging.info(f"Generating a list {n} users.")
    return [get_user() for _ in range(n)]


if __name__ == "__main__":
    users = get_users(3)
    print(users)
