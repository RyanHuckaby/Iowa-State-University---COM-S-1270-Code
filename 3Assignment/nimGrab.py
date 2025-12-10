"""
Ryan Huckaby
Date Started: 9/29/2025
Assignment #3
This code is an adaptation of the game "NIMGRAB!"
"""
from sys import exit
from random import randint

def whoseTurn(turn_number, first_player):
    if first_player in [0, 1]: #Human vs Human
        if (first_player == 0 and turn_number % 2 != 0) or (first_player == 1 and turn_number % 2 == 0):
            print("\nPlayer one is going...")
        else:
            print("\nPlayer two is going...")
    else: #Computer game
        if (first_player == 2 and turn_number % 2 != 0) or (first_player == 3 and turn_number % 2 == 0):
            print("\nPlayer is going...")
        else:
            print("\nComputer is going...")

def getWinner(turnNum, player):
    if player in [2, 3]:  # Computer Mode
        if (player == 2 and turnNum % 2 == 0) or (player == 3 and turnNum % 2 != 0):
            print("\nComputer took the last item. Player wins!\n")
        else:
            print("\nPlayer took the last item. Computer wins!\n")
    else:  # Human vs Human
        if (turnNum % 2 == 0 and player == 1) or (turnNum % 2 != 0 and player == 0):
            print("\nPlayer 1 took the last item. Player 2 wins!\n")
        else:
            print("\nPlayer 2 took the last item. Player 1 wins!\n")

def compTurn(amount):
    print("\nItems left:", amount)
    print("| " * amount)
    if amount <= 3:
        value = amount - 1 if amount > 1 else 1
    else:
        value = randint(1, 3)
    print(f"Computer takes: {value}")
    amount -= value
    return amount

def humanTurn(amount):
    print("\nItems left:", amount)
    print("| " * amount)
    while True:
        value = int(input("\nHow many items do you want to take [1-3]?: ").strip())
        if value < 1 or value > 3 or value > amount:
            print("ERROR: Invalid choice. Please choose again.")
        else:
            amount -= value
            break
    return amount

def turn(itemAmount, player, turn_number, choice):
    whoseTurn(turn_number, player)
    if choice == "c":
        if (player == 2 and turn_number % 2 != 0) or (player == 3 and turn_number % 2 == 0): #Human's Turn
            itemAmount = humanTurn(itemAmount)
            return itemAmount
        else:
            itemAmount = compTurn(itemAmount)            
            return itemAmount
    elif choice == "h":
        if (player == 0 and turn_number % 2 != 0) or (player == 1 and turn_number % 2 == 0): #Player 1's Turn
            itemAmount = humanTurn(itemAmount)
            return itemAmount
        else:
            itemAmount = humanTurn(itemAmount)
            return itemAmount
    return itemAmount

def main():
    print("NIMGRAB!\n\nBy: Ryan Huckaby\n[COM S 1270 2]\n")
    running = True
    while running:
        items = int(randint(20,25))
        choice1 = input("Do you want to [p]lay, read the [r]ules, or [q]uit?: ").lower().strip()
        if choice1 == "r":
            print("Rules of NIMGRAB\n" 
            "1. The goal is to avoid taking the last item. If you take the last item you lose.\n"
            "2. There will be 20-25 items in a row each time.\n"
            "3. Players alternate turns taking items.\n"
            "4. You may only take 1-3 items per turn.\n"
            "5. You can not take more items than remain.\n"
            "6. The computer will abide by the same rules... its just up to you."
            )
        elif choice1 == "q":
            print("Goodbye!")
            exit()
        elif choice1 == "p":
            choice2 = input("Do you want to play against [h]uman or [c]omputer?: ").lower().strip()
            if choice2 == "h":
                first_player = randint(0, 1)
            elif choice2 == "c":
                first_player = randint(2, 3)
            else:
                print("ERROR: Must input a valid input.")
                continue

            turn_number = 0
            while items > 0:
                turn_number += 1
                items = turn(items, first_player, turn_number, choice2)
            getWinner(turn_number, first_player)
        else:
            print("ERROR: Must input a valid input.")

if __name__ == "__main__":
    main()