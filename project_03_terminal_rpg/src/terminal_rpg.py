import random

MY_HEALTH = RIVAL_HEALTH = 50
MY_POTIONS = 3
SKIP_TURN = False

while True:

    if SKIP_TURN:
        print("You skip your turn!")
        SKIP_TURN = False

    else:
        choice = ""
        while choice not in ["1", "2"]:
            choice = input("Do you want to attack (1) or take a potion (2)? ")

        if choice == "1":
            my_attack = random.randint(5, 10)
            RIVAL_HEALTH -= my_attack
            print(
                f"You have inflicted {my_attack} points of damage on the enemy")

        elif choice == "2" and MY_POTIONS > 0:
            get_health_points = random.randint(15, 50)
            MY_HEALTH += get_health_points
            MY_POTIONS -= 1
            SKIP_TURN = True
            print(
                f"You get back {get_health_points} health points ({MY_POTIONS} potions remaining!)")
        else:
            print("You have no longer potions! You have to attack.")
            continue

    if RIVAL_HEALTH <= 0:
        print("Your enemy is dead! You are the winner!")
        break

    rival_attack = random.randint(5, 15)
    MY_HEALTH -= rival_attack
    print(
        f"The enemy has inflicted {rival_attack} damage points on you.")

    if MY_HEALTH <= 0:
        print("Game Over! You are the loser!")
        break

    print(f"You have {MY_HEALTH} health points remaining")
    print(f"The enemy have {RIVAL_HEALTH} points remaining")
    print(50 * "-")

print("End of the game!")
