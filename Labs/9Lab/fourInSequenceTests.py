"""
Ryan Huckaby
Lab #9 (Week Eleven)
Date Started: 11/5/2025
This code tests whether the functions from the connect four game work!
"""

import fourInSequence as f

def test_one():
    # DEBUGGING/ TESTING
    # "." "X" "O"
    # player 1 = X, 2 = O
    testBoard = [
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    ["X", "X", "X", "X", ".", ".", "."]]
    assert f.checkWinner(testBoard, 1) == True

def test_two():
    # DEBUGGING/ TESTING
    # "." "X" "O"
    # player 1 = X, 2 = O
    testBoard = [
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    ["X", ".", ".", ".", ".", ".", "."],
    ["X", ".", ".", ".", ".", ".", "."],
    ["X", ".", ".", ".", ".", ".", "."]]
    assert f.checkAdjacent(testBoard, 1) == 0

def test_three():
    # DEBUGGING/ TESTING
    # "." "X" "O"
    # player 1 = X, 2 = O
    testBoard = [
    ["X", "X", "X", "X", "X", "X", "X"],
    ["X", "X", "X", "X", "X", "X", "X"],
    ["X", "X", "X", "X", "X", "X", "X"],
    ["X", "X", "X", "X", "X", "X", "X"],
    ["X", "X", "X", "X", "X", "X", "X"],
    ["X", "X", "X", "X", "X", "X", "X"]]
    assert f.checkDraw(testBoard) == True

def test_four():
    # DEBUGGING/ TESTING
    # "." "X" "O"
    # player 1 = X, 2 = O
    testBoard = [
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", "X", ".", ".", ".", ".", "."],
    [".", "X", ".", ".", ".", ".", "."],
    [".", "X", ".", ".", ".", ".", "."]]
    assert f.checkForNextMoveWin(testBoard, 1) == 1
