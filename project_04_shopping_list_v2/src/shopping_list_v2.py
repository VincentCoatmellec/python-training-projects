import sys
import json
from pathlib import Path

SOURCE_FILE = Path(__file__).resolve()
CUR_DIR = SOURCE_FILE.parent.parent
DATA_FILE = CUR_DIR / "data" / "liste.json"

if DATA_FILE.exists():
    with open(DATA_FILE, "r") as f:
        LISTE = json.load(f)
else:
    LISTE = []

CHOICES = ["Add an item",
           "Remove an item",
           "Display my list",
           "Clear my list",
           "Quit"]

while True:

    print("Choose what you want to do: ")
    for i, item in enumerate(CHOICES, 1):
        print(f"{i}. {item}")
    user_choice = input("Your choice: ")

    if not user_choice.isdigit() or int(user_choice) > len(CHOICES) or int(user_choice) < 1:
        print("Your choice is not valid, please try again!")

    elif int(user_choice) == 1:
        item = input("What do you want to add in your list? ")
        LISTE.append(item.lower())
        print(f"Item '{item}' has been succefully added in your list!")

    elif int(user_choice) == 2:
        item = input("What item do you want to remove? ")
        if item.lower() in LISTE:
            LISTE.remove(item.lower())
            print(f"Item '{item}' has been succefully removed from your list!")
        else:
            print("This item is not in the list!")

    elif int(user_choice) == 3:
        if LISTE:
            print("Your shopping list: ")
            for i, item in enumerate(LISTE, 1):
                print(f"{i}. {item}")
        else:
            print("Your list is empty!")

    elif int(user_choice) == 4:
        LISTE.clear()
        print(f"Your list has been succefully cleared!")

    elif int(user_choice) == 5:
        DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(DATA_FILE, "w") as f:
            json.dump(LISTE, f, indent=4)
        print("See you later!")
        sys.exit()

    print(50 * "-")
