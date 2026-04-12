import logging
import json
from dataclasses import dataclass

from constants import DATA_DIR

LOGGER = logging.getLogger()


@dataclass
class Liste(list):
    name: str

    def add_item(self, item: str) -> bool:
        if not isinstance(item, str):
            raise ValueError("You can only add a string")

        if item in self:
            LOGGER.error(f"{item} is already in the list")
            return False

        self.append(item)
        return True

    def remove_item(self, item: str) -> bool:
        if item in self:
            self.remove(item)
            return True
        return False

    def display_list(self) -> None:
        print(f"My {self.name}'s list: ")
        for item in self:
            print(f" - {item}")

    def save_list(self) -> bool:
        DATA_DIR.mkdir(exist_ok=True)
        file = DATA_DIR / f"{self.name}.json"

        with open(file, "w") as f:
            json.dump(list(self), f, indent=4)

        return True

    def load_list(self) -> bool:
        file = DATA_DIR / f"{self.name}.json"

        if not file.exists():
            LOGGER.error(f"No file found for list '{self.name}'")
            return False

        with open(file, "r") as f:
            data = json.load(f)

        self.extend(data)
        return True

    def clear_list(self) -> None:
        self.clear()
        print(f"List '{self.name}' has been successfully cleared!")

    def delete_list(self) -> bool:
        file = DATA_DIR / f"{self.name}.json"

        if not file.exists():
            LOGGER.error(f"No file found for list '{self.name}'")
            return False

        file.unlink()
        self.clear()
        return True


def get_existing_lists() -> list:
    return [f.stem for f in DATA_DIR.iterdir() if f.suffix == ".json"]
