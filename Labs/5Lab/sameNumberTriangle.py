"""
Ryan Huckaby
Lab #5 (Week Six)
Date Started: 10/1/2025
This code creates a right angle triangle out of numbers.
"""
def sameNumberTriangle(n):
    for i in range(1, n+1):
        print(f"{i} " * i)
def main():
    num = int(input("Please enter an integer: "))
    sameNumberTriangle(num)
if __name__ == "__main__":
    main()