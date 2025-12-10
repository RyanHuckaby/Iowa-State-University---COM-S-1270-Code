"""
Ryan Huckaby
Lab #9 (Week Eleven)
Date Started: 11/5/2025
This code is a remake of the classic game rock-paper-scissors.
"""
import random

def generateComputerMove():
    moves = ["Rock", "Paper", "Scissors"]
    return random.choice(moves)

def determineWinner(humanMove, computerMove):
    if humanMove == computerMove:
        return "Draw"

    if humanMove == "Rock":
        if computerMove == "Paper":
            return "Paper"
        else: 
            return "Rock"

    if humanMove == "Paper":
        if computerMove == "Scissors":
            return "Scissors"
        else:
            return "Paper"

    if humanMove == "Scissors":
        if computerMove == "Rock":
            return "Rock"
        else: 
            return "Scissors"

def playRound(humanMove):
    computerMove = generateComputerMove()
    winner = determineWinner(humanMove, computerMove)

    if winner == "Draw":
        return "Draw"

    if winner == humanMove:
        return "Human Wins"

    return "Computer Wins"

def main():
    rounds = int(input("Enter an odd number of rounds: "))

    while rounds % 2 == 0:
        rounds = int(input("Please enter an odd number: "))

    humanWins = 0
    computerWins = 0
    roundsNeeded = rounds // 2 + 1

    while humanWins < roundsNeeded and computerWins < roundsNeeded:
        move = input("Your move (Rock, Paper, Scissors): ").lower().strip()
        result = playRound(move)

        if result == "Human Wins":
            humanWins += 1
            print("You win this round.")

        elif result == "Computer Wins":
            computerWins += 1
            print("Computer wins this round.")

        else:
            print("Round is a draw.")

        print("Score:", humanWins, "-", computerWins)

    if humanWins > computerWins:
        print("You win the match.")
    else:
        print("Computer wins the match.")

if __name__ == "__main__":
    main()