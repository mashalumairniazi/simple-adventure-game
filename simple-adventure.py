import random

# Introduction
print("Welcome to the Enhanced Adventure Game!")
name = input("What's your name? ")
print(f"Hello, {name}! Your journey begins now.")

# Start the game
while True:
    # Give choices
    print("\nYou find yourself at a crossroads. Where do you want to go?")
    print("1. Go left into the dark forest.")
    print("2. Go right towards the shining city.")
    print("3. Go straight ahead to the mountains.")
    choice = input("Enter 1, 2, or 3: ")

    # CHOICE 1 - forest
    if choice == "1":
        print(f"\n{name}, you venture into the dark forest and encounter a wild beast!")
        print("Do you want to fight the beast or run away? (fight/run)")
        choice = input("> ").lower()

        # Fight the beast
        if choice == "fight":
            print("You engage in combat with the beast.")
            player_health = 100
            print(f'Your health is: {player_health}')
            beast_health = 50
            print(f'The beast\'s health is: {beast_health}')

            # Attack or defend?
            while player_health > 0 and beast_health > 0:
                action = input("Do you want to attack or defend? (attack/defend) ").lower()

                # You attack the beast
                if action == "attack":
                    damage = random.randint(10, 30)
                    beast_health -= damage
                    print(f"You attack the beast and deal {damage} damage.")
                    print(f'The beast\'s health is: {beast_health}')
                    print('THE BEAST ATTACKS BACK')
                    damage = random.randint(15, 25)
                    print(f"The beast attacks you and deals {damage} damage.")
                    player_health -= damage
                    print(f'Your health is: {player_health}')

                # You defend yourself
                elif action == "defend":
                    print("You defend yourself, reducing incoming damage.")
                    damage = random.randint(5, 20)
                    defend = random.randint(1, 10)
                    print(f"The beast attacks you and deals {damage} damage.")
                    print(f'You block {defend} damage.')
                    player_health -= max(0, damage - defend)
                    print(f'Your health is: {player_health}')

                else:
                    print("Invalid action. The beast attacks you.")
                    damage = random.randint(10, 20)
                    player_health -= damage
                    print(f"The beast deals {damage} damage.")
                    print(f'Your health is: {player_health}')

            if player_health > 0:
                print("You defeated the beast! Congratulations!")
            else:
                print("You were defeated by the beast. Game over.")
            break

        # Run away
        else:
            print("You run away safely and return to the crossroads.")

    # CHOICE 2 - city
    elif choice == "2":
        print(f"\n{name}, you walk towards the city and encounter a cunning thief!")
        print("Do you want to fight the thief or run away? (fight/run)")
        choice = input("> ").lower()

        # Fight the thief
        if choice == "fight":
            print("You engage in combat with the thief.")
            player_health = 100
            print(f'Your health is: {player_health}')
            thief_health = 50
            print(f'The thief\'s health is: {thief_health}')

            # Attack or defend?
            while player_health > 0 and thief_health > 0:
                action = input("Do you want to attack or defend? (attack/defend) ").lower()

                # You attack the thief
                if action == "attack":
                    damage = random.randint(10, 30)
                    thief_health -= damage
                    print(f"You attack the thief and deal {damage} damage.")
                    print(f'The thief\'s health is: {thief_health}')
                    print('THE THIEF ATTACKS BACK')
                    damage = random.randint(15, 25)
                    print(f"The thief attacks you and deals {damage} damage.")
                    player_health -= damage
                    print(f'Your health is: {player_health}')

                # You defend yourself
                elif action == "defend":
                    print("You defend yourself, reducing incoming damage.")
                    damage = random.randint(5, 20)
                    defend = random.randint(1, 10)
                    print(f"The thief attacks you and deals {damage} damage.")
                    print(f'You block {defend} damage.')
                    player_health -= max(0, damage - defend)
                    print(f'Your health is: {player_health}')

                else:
                    print("Invalid action. The thief attacks you.")
                    damage = random.randint(10, 20)
                    player_health -= damage
                    print(f"The thief deals {damage} damage.")
                    print(f'Your health is: {player_health}')

            if player_health > 0:
                print("You defeated the thief! Congratulations!")
            else:
                print("You were defeated by the thief. Game over.")
            break
        

        # Run away
        else:
            print("You run away safely and return to the crossroads.")

    # CHOICE 3 - mountains
    elif choice == "3":
        print(f"\n{name}, you climb the mountains and encounter a fierce eagle!")
        print("Do you want to fight the eagle or run away? (fight/run)")
        choice = input("> ").lower()

        # Fight the eagle
        if choice == "fight":
            print("You engage in combat with the eagle.")
            player_health = 100
            print(f'Your health is: {player_health}')
            eagle_health = 50
            print(f'The eagle\'s health is: {eagle_health}')

            # Attack or defend?
            while player_health > 0 and eagle_health > 0:
                action = input("Do you want to attack or defend? (attack/defend) ").lower()

                # You attack the eagle
                if action == "attack":
                    damage = random.randint(10, 30)
                    eagle_health -= damage
                    print(f"You attack the eagle and deal {damage} damage.")
                    print(f'The eagle\'s health is: {eagle_health}')
                    print('THE EAGLE ATTACKS BACK')
                    damage = random.randint(15, 25)
                    print(f"The eagle attacks you and deals {damage} damage.")
                    player_health -= damage
                    print(f'Your health is: {player_health}')

                # You defend yourself
                elif action == "defend":
                    print("You defend yourself, reducing incoming damage.")
                    damage = random.randint(5, 20)
                    defend = random.randint(1, 10)
                    print(f"The eagle attacks you and deals {damage} damage.")
                    print(f'You block {defend} damage.')
                    player_health -= max(0, damage - defend)
                    print(f'Your health is: {player_health}')

                else:
                    print("Invalid action. The eagle attacks you.")
                    damage = random.randint(10, 20)
                    player_health -= damage
                    print(f"The eagle deals {damage} damage.")
                    print(f'Your health is: {player_health}')

            if player_health > 0:
                print("You defeated the eagle! Congratulations!")
            else:
                print("You were defeated by the eagle. Game over.")
            break

        # Run away
        else:
            print("You run away safely and return to the crossroads.")

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

print(f"\nThank you for playing, {name}! Your adventure ends here.")

#THE ENDDD
