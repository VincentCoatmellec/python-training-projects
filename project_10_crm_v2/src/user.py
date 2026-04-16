from dataclasses import dataclass
from tinydb import TinyDB, where
from tinydb.table import Document
from pathlib import Path
import re
import string


@dataclass
class User:

    DB = TinyDB(Path(__file__).resolve().parent / "db.json", indent=4)

    first_name: str
    last_name: str
    phone_number: str = ""
    adress: str = ""

    def __repr__(self) -> str:
        return f"User({self.first_name}, {self.last_name})"

    def __str__(self) -> str:
        return f"{self.full_name}\n{self.phone_number}\n{self.adress}"

    @property
    def full_name(self) -> str:
        """Function to get the full name of the user

        Returns:
            str: The full name of the user
        """
        return f"{self.first_name} {self.last_name}"

    @property
    def db_instance(self) -> Document | list[Document] | None:
        """Function to get the database instance of the user

        Returns:
            Document | list[Document] | None: The database instance of the user
        """
        return User.DB.get((where("first_name") == self.first_name) & (where("last_name") == self.last_name))

    def _checks(self) -> None:
        """ Function to check the validity of the data

            Raises:
                ValueError: If the data is invalid
        """
        self._check_names()
        self._check_phone_number()

    def _check_phone_number(self) -> None:
        """Function to check the validity of the phone number

        Raises:
            ValueError: If the phone number is invalid
        """
        phone_number = re.sub(r"[+()\s]*", "", self.phone_number)
        if len(phone_number) < 10 or not phone_number.isdigit():
            raise ValueError(
                f"Numéro de téléphone {self.phone_number} invalid")

    def _check_names(self) -> None:
        """Function to check the validity of the names

        Raises:
            ValueError: If the names are invalid
        """
        if not (self.first_name and self.last_name):
            raise ValueError("Le prénom et le nom ne peuvent pas être vide")

        special_characters = string.digits + string.punctuation

        if any(character in special_characters for character in self.first_name + self.last_name):
            raise ValueError(f"Nom invalide {self.full_name}")

    def exists(self) -> bool:
        """ Function to check if the user exists in the database

        Returns:
            bool: True if the user exists in the database, False otherwise
        """
        return bool(self.db_instance)

    def delete(self) -> list[int]:
        """ Function to delete the user from the database

        Returns:
            list[int]: The list of deleted document ids
        """
        doc = self.db_instance
        if isinstance(doc, Document):
            return User.DB.remove(doc_ids=[doc.doc_id])
        return []

    def save(self, validate_data: bool = False) -> int:
        """ Function to save the user in the database

        Args:
            validate_data (bool, optional): Whether to validate the data before saving. Defaults to False.

        Returns:
            int: The ID of the saved document, or -1 if the user already exists
        """
        if validate_data:
            self._checks()

        if self.exists():
            return -1
        else:
            return User.DB.insert(self.__dict__)


def get_all_users() -> list[User]:
    """ Function to get all the users from the database

    Returns:
        list[User]: The list of all the users from the database
    """
    return [User(**user) for user in User.DB.all()]


if __name__ == "__main__":
    pass
