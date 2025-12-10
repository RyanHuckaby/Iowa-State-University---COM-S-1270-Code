"""
Ryan Huckaby
Lab #4 (Week Five)
Date Started: 9/24/2025
This code writes a short interactive 'story' using if statements and user inputs for what to happen.
"""
def main():
    print('\nWelcome to "Horrors of Count Dracula"\nBy: Ryan Huckaby\n')
    running = True
    while running:
#First Choice
        choice_one = input("You are awaken abruptly and find yourself surrounded by a violent mob with garlic and pitchforks.\nDazed you search for a way out... What do you do?:\n1. Try to talk with the villagers and see if they'll let you go.\n2. Turn into a bat and fly away.\n3. Fight your way out (this decision will not end well...).\n4. Stand and do nothing.\n")
        if choice_one == "1":
            choice_one_one = input("\nYou converse with the villagers and get them to lower their guards...\n*Influence with townsfolk +1*\nThey continue to ask more about you... What do you do?\n1. Tell them the truth.\n2. Mix in some lies with the truth.\n3. Fly away.\n")
            if choice_one_one == "1":
                choice_two = input("\nThe villagers look shocked as you reveal your dark nature, but some begin to pity you...\nDo you:\n1. Beg for mercy.\n2. Attempt to convert them to your side.\n3. Try to hypnotize their leader.\n")
                if choice_two == "1":
                    cont = input("\nThey laugh at your weakness and strike you down.\nYou are dead.\n\nWould you like to start again?\n Y / N\n").lower()
                    if cont == "n":
                        running = False
                elif choice_two == "2":
                    input("\nThe villagers hesitate, but then drive a stake through your chest.\nYou are dead.\n")
                elif choice_two == "3":
                    choice_three = input("\nYour eyes glow red as you focus on their leader...\nHe begins to falter.\nDo you:\n1. Command him to attack the other villagers.\n2. Command him to free you.\n")
                    if choice_three == "1":
                        input("\nThe leader turns and attacks his own people. Chaos erupts. In the confusion, you escape into the night.\nEnding: You Survived.\n")
                        running = False
                    elif choice_three == "2":
                        cont = input("\nHe cuts your bonds, but the other villagers quickly kill him and turn on you.\nYou are dead.\n\nWould you like to start again?\n Y / N\n").lower()
                        if cont == "n":
                            running = False
                    else:
                        print("Make sure you pick an option 1 or 2.")
                        running = False
            elif choice_one_one == "2":
                cont = input("\nThey sense your deception and turn hostile again.\nYou are killed.\n\nWould you like to start again?\n Y / N\n").lower()
                if cont == "n":
                    running = False
            elif choice_one_one == "3":
                cont = input("\nAs you transform, an arrow pierces your wing. You fall to the ground and are trampled.\nYou are dead.\n\nWould you like to start again?\n Y / N\n").lower()
                if cont == "n":
                    running = False
            else:
                print("Make sure you pick an option 1, 2, or 3.")
                running = False
#Second Choice
        elif choice_one == "2":
            choice_one_two = input("\nYou have been shot with an arrow by an archer above after you transformed\n*Flying has failed*\n*Influence with townsfolk -2 (They grow angrier)*\nWhat do you do next?\n1. Try to talk with the villagers and see if they'll let you go.\n2. Fight your way out (this decision will not end well).\n3. Stand and do nothing.\n")
            if choice_one_two == "1":
                cont = input("\nYou lash out, but the mob overwhelms you with sheer numbers.\nYou are dead.\n\nWould you like to start again?\n Y / N\n").lower()
                if cont == "n":
                    running = False
            elif choice_one_two == "2":
                cont = input("\nYou lash out, but the mob overwhelms you with sheer numbers.\nYou are dead.\n\nWould you like to start again?\n Y / N\n").lower()
                if cont == "n":
                    running = False
            elif choice_one_two == "3":
                cont = input("\nYou are driven into a corner and the villagers get the best of you...\n\nYou have died...\n\nWould you like to start again?\n Y / N\n").lower()
                if cont == "n":
                    running = False
            else:
                print("Make sure you pick an option 1, 2, or 3.")
                running = False
#Third Choice
        elif choice_one == "3":
            cont = input("\nYou fight with all your strength, but the mob outnumbers you.\nThey strike you down.\nYou are dead.\nWould you like to start again?\n Y / N\n").lower()
            if cont == "n":
                running = False
#Fourth Choice
        elif choice_one == "4":
            cont = input("\nYou stand motionless, paralyzed with fear.\nThe mob advances and tears you apart.\nYou are dead.\nWould you like to start again?\n Y / N\n").lower()
            if cont == "n":
                running = False
        else: 
            print("Make sure you pick an option 1, 2, 3, or 4.")
            running = False
if __name__ == "__main__":
    main()