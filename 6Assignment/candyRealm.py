# Ryan Huckaby            11-25-2025
# Assignment #6
#
# Description: This is the code for a game that involves four players and each player must race to the end of the 'board'
#              The first person to reach the end wins! (Similiar to the board game 'Candy Crush' -- what this game is based on.)

from sys import exit
import colorama as c
import random as r

c.init()

def colorBoard(total_spaces):
    colored = []
    for char in total_spaces:
        if char == "R":
            colored.append(c.Fore.RED + "R")
        elif char == "M":
            colored.append(c.Fore.MAGENTA + "M")
        elif char == "Y":
            colored.append(c.Fore.YELLOW + "Y")
        elif char == "C":
            colored.append(c.Fore.CYAN + "C")
        elif char == "W":
            colored.append(c.Fore.WHITE + "W")
        elif char == "G":
            colored.append(c.Fore.GREEN + "G")
            
    return "  " + "  ".join(colored) + c.Fore.WHITE


def printBoard(total_spaces, cards, position):

    board = colorBoard(total_spaces)

    colored_cards = colorBoard(cards.copy())

    print("\n"
f"{' ' * (8 + position[1] * 3)}1\n"
f"{' ' * (8 + position[2] * 3)}2\n"
f"{' ' * (8 + position[3] * 3)}3\n"
f"{' ' * (8 + position[4] * 3)}4\n"
" START" + f"{board}" + "  GOAL!\n"
" CARDS" + colored_cards
)

def getTurn(players, cards, total_spaces):

    position = {}
    for i in range(1, 5):
        position[i] = 0
    
    top_card = cards[0]

    while True:
        for i in range(1, players + 1): #human

            printBoard(total_spaces, cards, position)
            while True:
                choice = input((f"\nPlayer {i}: Would you like to [d]raw a '{top_card}' card, [s]huffle the deck, or [q]uit?: ")).strip().lower()
                if choice in ["d", "s", "q"]:
                    break
            if choice == "d":

                old_position = position[i]

                for j in range(position[i] + 1, len(total_spaces)):
                    if total_spaces[j] == top_card and j > position[i]:
                        position[i] = j
                        break
                
                card_used = top_card
                drawn_card = cards.pop(0)
                cards.append(drawn_card)
                top_card = cards[0] 

                spaces_moved = position[i] - old_position
            
                print(f"\nPlayer {i} (HUMAN) has drawn '{card_used}'!")
                print(f"Player {i} (HUMAN) has moved forward {spaces_moved} spaces!")

                if position[i] >= len(total_spaces) - 1:
                    print(f"\nCongratulations! Player {i} has reached the last square and wins!")

                    printBoard(total_spaces, cards, position)

                    return

                while True:
                    if input("\nPress Enter to continue...")== "":
                        break
                    else:
                        print("Please press 'Enter' to move on to the next turn.")

            elif choice == "s":

                print(f"\nPlayer {i} (HUMAN) has shuffled the deck!")
                
                while True:
                    if input("\nPress Enter to continue...") == "":
                        break
                    else:
                        print("Please press 'Enter' to move on to the next turn.")

                r.shuffle(cards)
                top_card = cards[0]

            elif choice == "q":
                print("\nGoodbye!\n")
                exit()

        for i in range(players + 1, 5): 

            spaces_beyond = total_spaces[position[i] + 1:]

            printBoard(total_spaces, cards, position)

            matching_space = -1
            for j in range(position[i] + 1, len(total_spaces)):
                if total_spaces[j] == top_card:
                    matching_space = j
                    break

            if matching_space == len(total_spaces) - 1:
                old_position = position[i]

                position[i] = len(total_spaces) - 1
                spaces_moved = position[i] - old_position


                card_used = top_card
                drawn_card = cards.pop(0)
                cards.append(drawn_card)
                top_card = cards[0]
                
                spaces_moved = position[i] - old_position
                
                print(f"\nPlayer {i} (COMPUTER) has drawn: {card_used}" + c.Fore.WHITE)
                print(f"Player {i} (COMPUTER) has moved forward {spaces_moved} spaces!" + c.Fore.WHITE)

                print(f"\nComputer Player {i} has reached the last square and wins!")

                printBoard(total_spaces, cards, position)

                if position[i] >= len(total_spaces) - 1:
                        print(f"\nComputer Player {i} has reached the last square and wins!")

                        printBoard(total_spaces, cards, position)

                        return

            elif top_card not in spaces_beyond:
                    
                    print(f"\nPlayer {i} (COMPUTER) has shuffled the deck!")
                    r.shuffle(cards)
                    top_card = cards[0]

            else:
                move = r.randint(0, 1)
                if move == 0:

                    old_position = position[i]

                    for j in range(position[i] + 1, len(total_spaces)):
                        if total_spaces[j] == top_card and j > position[i]:
                            position[i] = j
                            break
                    
                    spaces_moved = position[i] - old_position

                    card_used = top_card
                    drawn_card = cards.pop(0)
                    cards.append(drawn_card)
                    top_card = cards[0]  

                    print(f"\nPlayer {i} (COMPUTER) has drawn: {card_used}" + c.Fore.WHITE)
                    print(f"Player {i} (COMPUTER) has moved forward {spaces_moved} spaces!" + c.Fore.WHITE)

                    if position[i] >= len(total_spaces) - 1:
                        print(f"\nComputer Player {i} has reached the last square and wins!")

                        printBoard(total_spaces, cards, position)

                        return

                elif move == 1:
                    print(f"\nPlayer {i} (COMPUTER) has shuffled the deck!")
                    r.shuffle(cards)
                    top_card = cards[0]

                elif position[i] >= len(total_spaces) - 1:
                    print(f"Computer Player {i} wins!")
                    exit()

            while True:
                if input("\nPress Enter to continue...") == "":
                    break
                else:
                    print("Please press 'Enter' to move on to the next turn.")

def getValues():
    while True:
        players_input = input("How Many Human Players [1] - [4]?: ").strip()

        if not players_input.isdigit():
            print("\nError: Please enter a whole number.\n")
            continue

        players = int(players_input)
        if not (0 <= players <= 4):
            print("\nError: Number of players must be between 1 and 4.\n")
            continue
        break

    while True:
        copies_input = input("\nHow Many Copies Of Each Card [1] - [5]?: ").strip()

        if not copies_input.isdigit():
            print("\nError: Please enter a whole number.\n")
            continue

        copies = int(copies_input)
        if not (1 <= copies <= 5):
            print("\nError: Number of copies must be between 1 and 5.\n")
            continue
        break

    return players, copies
        
def selection():
    running = True

    while running:
        print("\n-----------------------------------------------------------------")
        choice = input("\nMAIN MENU: [p]lay game, [i]nstructions, or [q]uit?: ").lower().strip()
        print()

        if choice == "i":
            print(
            "How to Win: \n\n"
            "Be the first to reach the castle at the end of the board!\n" 
            "You must pull the exact color of the last space to move there and win.\n\n" 
            "How to Play:\n\n"
            "1. On your turn, draw the top card from the deck.\n"
            "2. Move to the next space that matches the color on the card.\n\n"
            )

        elif choice == "p":
            return "p"
        
        elif choice == "q":
            running = False
            print("Goodbye!\n")
            exit()

        else:
            print("Please enter [p], [i], or [q]...\n")

def main():
    print("\nCandy Realm!\n\nBy: Ryan Huckaby\n[COM S 1270 2]")

    while True:
        choice = selection()
        if choice == "q":
            print("Goodbye!\n")
            exit()
        elif choice == "p":
            players, copies = getValues()

        colors = ["R", "M", "Y", "C", "W", "G"]

        total_spaces = colors * copies

        r.shuffle(total_spaces)

        cards = total_spaces.copy()
        r.shuffle(cards)

        getTurn(players, cards, total_spaces)

if __name__ == "__main__":
    main()