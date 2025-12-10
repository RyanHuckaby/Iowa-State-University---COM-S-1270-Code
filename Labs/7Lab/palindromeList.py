"""
Ryan Huckaby
Lab #7 (Week Eight)
Date Started: 10/15/2025
This code will check if the list itself is a palindrome.
"""
def palindromeList(l1):
    for i in range(len(l1)):
        if l1[i] == l1[(i-1)]:
            x = True
        else:
            x = False
        return x
def getInput():
    palList = []
    while True:
        inp1 = input("What would you like to input: ")
        if inp1 == "*":
            break
        else:
            palList.append(inp1)
    return palList
def main():
    l2 = getInput()
    if palindromeList(l2):
        print("Your list is a palindrome!")
    else:
        print("Your list is NOT a palindrome!")
if __name__ == "__main__":
    main()