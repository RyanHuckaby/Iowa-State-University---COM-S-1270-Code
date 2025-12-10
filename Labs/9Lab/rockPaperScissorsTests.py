"""
Ryan Huckaby
Lab #9 (Week Eleven)
Date Started: 11/5/2025
This code tests whether functions from our previously made rock-paper-scissors work!
"""
import pytest
import rockPaperScissors as rps
 
def test_generateComputerMove():
    move = rps.generateComputerMove()
    assert move in ["Rock", "Paper", "Scissors"]

def test_determineWinner():
    assert rps.determineWinner("Rock", "Paper") == "Paper"
    assert rps.determineWinner("Rock", "Scissors") == "Rock"
    assert rps.determineWinner("Paper", "Scissors") == "Scissors"
    assert rps.determineWinner("Paper", "Rock") == "Paper"
    assert rps.determineWinner("Scissors", "Rock") == "Rock"
    assert rps.determineWinner("Scissors", "Paper") == "Scissors"
    assert rps.determineWinner("Rock", "Rock") == "Draw"

def test_playRound():
    result = rps.playRound("Rock")
    assert result in ["Human Wins", "Computer Wins", "Draw"]