"""
Ryan Huckaby
Lab #5 (Week Six)
Date Started: 10/1/2025
This code creates a multiplication table depending on user input
"""
def multiplicationTable(a, b):
    for i in range(a, b+1):
        for j in range(1, b+1):
            print('{0:4d}'.format(i*j), end="")
        print()
def main():
    lowNum = int(input("Please input an integer: "))
    highNum = int(input("Please input an integer: "))
    multiplicationTable(lowNum, highNum)
if __name__ == "__main__":
    main()