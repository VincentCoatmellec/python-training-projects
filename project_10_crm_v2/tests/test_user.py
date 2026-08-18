from src.user import User
import pytest
from tinydb import TinyDB, table
from tinydb.storages import MemoryStorage


@pytest.fixture
def setup_db():
	User.DB = TinyDB(storage=MemoryStorage)


@pytest.fixture
def user(setup_db):
	u = User(first_name="Patrick",
	         last_name="Smith",
	         address="1 rue du Chemin, 75001 Paris",
	         phone_number="+44 555 555 555")
	u.save()
	return u


def test_full_name(user: User):
	assert user.full_name == "Patrick Smith"


def test_exists(user: User):
	assert user.exists() is True


def test_not_exists(setup_db):
	u = User(first_name="Patrick",
	         last_name="Smith",
	         address="1 rue du Chemin, 75001 Paris",
	         phone_number="+44 555 555 555")
	assert u.exists() is False


def test_db_instance(user: User):
	instance = user.db_instance
	assert isinstance(instance, table.Document)
	assert instance["first_name"] == "Patrick"
	assert instance["last_name"] == "Smith"
	assert instance["address"] == "1 rue du Chemin, 75001 Paris"
	assert instance["phone_number"] == "+44 555 555 555"


def test_not_db_instance(setup_db):
	u = User(first_name="Patrick",
	         last_name="Smith",
	         address="1 rue du Chemin, 75001 Paris",
	         phone_number="+44 555 555 555")
	assert u.db_instance is None


def test__check_phone_number(setup_db):
	user_good = User(first_name="Jean",
	                 last_name="Smith",
	                 address="1 rue du Chemin, 75001 Paris",
	                 phone_number="+44 555 555 555")
	user_bad = User(first_name="Jean",
	                last_name="Smith",
	                address="1 rue du Chemin, 75001 Paris",
	                phone_number="abcd")
	with pytest.raises(ValueError) as err:
		user_bad._check_phone_number()
	assert "invalid" in str(err.value)

	user_good.save(validate_data=True)
	assert user_good.exists() is True


def test__check_names_empty(setup_db):
	user_bad = User(first_name="",
	                last_name="",
	                address="1 rue du Chemin, 75001 Paris",
	                phone_number="+44 555 555 555")
	with pytest.raises(ValueError) as err:
		user_bad._check_names()
	assert "First name and last name are required" in str(err.value)


def test__check_names_invalid_characters(setup_db):
	user_bad = User(first_name="Patrick*(%",
	                last_name="%%%%",
	                address="1 rue du Chemin, 75001 Paris",
	                phone_number="+44 555 555 555")
	with pytest.raises(ValueError) as err:
		user_bad._check_names()
	assert "Invalid name" in str(err.value)


def test_delete(setup_db):
	user_test = User(first_name="Patrick",
	                 last_name="Smith",
	                 address="1 rue du Chemin, 75001 Paris",
	                 phone_number="+44 555 555 555")
	user_test.save()
	first = user_test.delete()
	second = user_test.delete()
	assert len(first) > 0
	assert isinstance(first, list)
	assert len(second) == 0
	assert isinstance(second, list)


def test_save(setup_db):
	user_test = User(first_name="Patrick",
	                 last_name="Smith",
	                 address="1 rue du Chemin, 75001 Paris",
	                 phone_number="+44 555 555 555")
	user_test_duplicate = User(first_name="Patrick",
	                           last_name="Smith",
	                           address="1 rue du Chemin, 75001 Paris",
	                           phone_number="+44 555 555 555")
	first = user_test.save()
	second = user_test_duplicate.save()
	assert isinstance(first, int)
	assert isinstance(second, int)
	assert first > 0
	assert second == -1
