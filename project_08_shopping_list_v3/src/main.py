import sys
from lib import Liste, get_existing_lists
from constants import MENU

# --- List selection at startup ---
existing_lists = get_existing_lists()

if existing_lists:
    print("Existing lists:")
    for i, name in enumerate(existing_lists, 1):
        print(f"{i}. {name}")
    print(f"{len(existing_lists) + 1}. Create a new list")

    user_choice = input("Your choice: ")

    if user_choice.isdigit() and 1 <= int(user_choice) <= len(existing_lists):
        ma_liste = Liste(name=existing_lists[int(user_choice) - 1])
        ma_liste.load_list()
    else:
        name = input("Name of your new list: ")
        ma_liste = Liste(name=name)
else:
    print("No existing list found, creating a new one!")
    name = input("Name of your new list: ")
    ma_liste = Liste(name=name)

print(50 * "-")

# --- Main menu ---
while True:
    print(f"Current list: {ma_liste.name}")
    print("Choose what you want to do: ")
    for i, choice in enumerate(MENU, 1):
        print(f"{i}. {choice}")

    user_choice = input("Your choice: ")

    if not user_choice.isdigit() or not (1 <= int(user_choice) <= len(MENU)):
        print("Your choice is not valid, please try again!")

    elif int(user_choice) == 1:
        item = input("What do you want to add? ")
        ma_liste.add_item(item.lower())

    elif int(user_choice) == 2:
        item = input("What item do you want to remove? ")
        ma_liste.remove_item(item.lower())

    elif int(user_choice) == 3:
        ma_liste.display_list()

    elif int(user_choice) == 4:
        ma_liste.clear_list()

    elif int(user_choice) == 5:
        ma_liste.delete_list()
        print(f"List '{ma_liste.name}' has been successfully deleted!")
        sys.exit()

    elif int(user_choice) == 6:
        ma_liste.save_list()
        print("See you later!")
        sys.exit()

    elif int(user_choice) == 7:
        print("Quit without saving!")
        sys.exit()

    print(50 * "-")
