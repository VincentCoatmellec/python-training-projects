import random

a, b = 0, 100
attempts = 5
mystery_number = random.randint(a, b)

print("*** Welcome to the mystery number game ***")
print(f"Find the mystery number! It is between {a} and {b}!")
print(f"You have {attempts} attempts left")

while not attempts == 0:

    choice = input("What number do you want to choice? ")

    if not choice.isdigit():
        print("Please choose a valid number")
        print(f"You have {attempts} attempts left")
        print(30 * "-")

    elif (int(choice) < a or int(choice) > b):
        print("Please choose a number in the range")
        print(f"You have {attempts} attempts left")
        print(30 * "-")

    elif int(choice) == mystery_number:
        print(
            f"Well done! You have found the mystery number with {attempts} attempts!")
        print("The game is terminated")
        print(30 * "-")
        break

    elif int(choice) > mystery_number:
        print(f"The mystery number is lower than {choice}")
        attempts -= 1
        print(f"You have {attempts} attempts left")
        print(30 * "-")

    else:
        print(f"The mystery number is bigger than {choice}")
        attempts -= 1
        if attempts == 0:
            print("You have no longer attempts")
            print(f"The mystery number was {mystery_number}")
            print("Game over!")
            break
        else:
            print(f"You have {attempts} attempts left")
            print(30 * "-")
