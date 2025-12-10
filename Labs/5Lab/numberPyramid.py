"""
Ryan Huckaby
Lab #5 (Week Six)
Date Started: 10/1/2025
This code creates an equailateral triangle out of numbers.
"""
def numberPyramid(n):
    for i in range(1, n+1):
        print(" " * (n-i), end="")
        for j in range(1, i+1):
            print(f"{j} ", end="")
        print()
def main():
    num = int(input("Please enter an integer: "))
    numberPyramid(num)
if __name__ == "__main__":
    main()