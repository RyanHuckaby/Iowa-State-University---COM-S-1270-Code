"""
Ryan Huckaby
Date Started: 9/10/2025
Assignment #2
This code, a rudimentary calculator, is going to take inputs from the user and ask them to choose either a 
basic math operation (+, -, *, /, //, %, **), or to choose to print out a 'lucky number.'
"""
import random
print("Lucky Calculator!\n\nBy: Ryan Huckaby\n[COM S 1270 2]\n\nWhich option would you like to select?\n")
var = str(input(f"Option 1: Calculator\nOption 2: Lucky number!?\nOption 3: Quit\nI would like to select option (1, 2, 3): "))
if var not in ["1", "2", "3"]:
    print("It seems your Input wasn't quite right... make sure you choose a number 1, 2 or 3.")
ans = 0
if var == "1":
    operation = str(input("\nPlease Choose a Calculation [+], [-], [*], [/], [//], [%], [**]: "))
    if operation not in ["+", "-", "*", "/", "//", "%", "**"]:
            print("Oops something went wrong! You MUST use [+], [-], [*], [/], [//], [%], or [**]")
    else:
        n1 = int(input("Please Enter Your First Integer: "))
        n2 = int(input("Please Enter Your Second Integer: "))
        if operation == "+":
                ans = n1 + n2
        elif operation == "-":
                ans = n1 - n2
        elif operation == "*":
                ans = n1 * n2
        elif operation == "/":
                if n2 == 0:
                    print("ERROR // Second variable = 0 changed to 1")
                    n2 = 1
                ans = n1 / n2
        elif operation == "//": #returns only the int version of a division problem
                if n2 == 0:
                    print("ERROR // Second variable = 0 changed to 1")
                    n2 = 1
                ans = n1 // n2
        elif operation == "%": #returns the remainder of divison problem
                if n2 == 0:
                    print("ERROR // Second variable = 0 changed to 1")
                    n2 = 1
                ans = n1 % n2
        elif operation == "**":
                ans = n1 ** n2
        print(f"The result of ({n1} {operation} {n2}) is: {ans}")
if var == "2":
    l1 = int(input("Please Enter an Integer: "))
    l2 = int(input("Please Enter an Integer: "))
    print(f"Your random number is: {random.randint(l1,l2+1)}")
if var == "3":
    print("Goodbye!")