"""
Ryan Huckaby
Lab #7 (Week Eight)
Date Started: 10/15/2025
This code finds the minimum and maximum values of numbers.
"""
def findMin(list):
    min = list[0]
    for s in list[1:]:
        if s < min:
            min = s
    return min
def findMax(list):
    max = list[0]
    for s in list[1:]:
        if s > max:
            max = s
    return max
def getInput():
    numbers = []
    while True:
        inp1 = input("What number would you like to input: ")
        if inp1 == "*":
            break
        else:
            numbers.append(int(inp1))
    return numbers
def main():
    l1 = getInput()
    min = findMin(l1)
    max = findMax(l1)
    print(f"Your Minimum Value is: {min}\nYour Maximum Value is: {max}")
if __name__ == "__main__":
    main()