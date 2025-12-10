"""
Ryan Huckaby
Lab #7 (Week Eight)
Date Started: 10/15/2025
This code will take numbers from the user and rotate them as the user desires.
"""
def rotateList(l1, n):
    n = int(n)
    if n == 0:
        return l1
    
    elif n > 0:
        for i in range(n):
            remove = l1.pop(-1)
            l1.insert(0, remove)
        return l1
    
    elif n < 0:
        for i in range(abs(n)):
            remove = l1.pop(0)
            l1.append(remove)
        return l1
    
    return l1
def getInput():
    intList = []
    while True:
        inp1 = input("What number would you like to input: ")
        if inp1 == "*":
            break
        else:
            intList.append(str(inp1))
    return intList
def main():
    l2 = getInput()
    rot = input("Please enter an integer: ")
    my_list = rotateList(l2, rot)
    my_list = [int(x) for x in my_list]
    print(my_list, sep=',')
if __name__ == "__main__":
    main()