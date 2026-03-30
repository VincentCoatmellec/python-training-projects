# PROJECT 3
import sys

CHOICES = ["Add an item",
           "Remove an item",
           "Display my list",
           "Clear my list",
           "Quit"]

SHOPPING_LIST = []

while True:

    print("Choose what you want to do: ")
    for i, item in enumerate(CHOICES, 1):
        print(f"{i}. {item}")
    user_choice = input("Your choice: ")

    if not user_choice.isdigit() or int(user_choice) > len(CHOICES) or int(user_choice) < 1:
        print("Your choice is not valid, please try again!")

    elif int(user_choice) == 1:
        item = input("What do you want to add in your list? ")
        SHOPPING_LIST.append(item.lower())
        print(f"Item '{item}' has been succefully added in your list!")

    elif int(user_choice) == 2:
        item = input("What item do you want to remove? ")
        if item.lower() in SHOPPING_LIST:
            SHOPPING_LIST.remove(item.lower())
            print(f"Item '{item}' has been succefully removed from your list!")
        else:
            print("This item is not in the list!")

    elif int(user_choice) == 3:
        if SHOPPING_LIST:
            print("Your shopping list: ")
            for i, item in enumerate(SHOPPING_LIST, 1):
                print(f"{i}. {item}")
        else:
            print("Your list is empty!")

    elif int(user_choice) == 4:
        SHOPPING_LIST.clear()
        print(f"Your list has been succefully cleared!")

    elif int(user_choice) == 5:
        print("See you later!")
        sys.exit()

    print(50 * "-")
