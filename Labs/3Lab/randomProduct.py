"""
Ryan Huckaby
Lab #3 (Week Four)
Date Started: 9/17/2025
This code uses inputs from the user to multiply a changing numbers of random variables and then prints it out using the "if" function and the variable "__main__".
"""
import random
def randomProduct(a, b, c):
    ans = 1
    for i in range(0, a):
        ans *= (random.randrange(b, c+1))
    return ans
def main():
    amount = int(input("Please choose how many random integers you want to multiply: "))
    int1 = int(input("Please input an integer: "))
    int2 = int(input("Please input an integer: "))  
    print(f"The answer is: {randomProduct(amount, int1, int2)}")
if __name__ == "__main__":
    main()