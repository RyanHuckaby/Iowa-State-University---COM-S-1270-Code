"""
Ryan Huckaby
Lab #7 (Week Eight)
Date Started: 10/15/2025
This code will take numbers the user and move specific numbers to the end of the list.
"""
def endNum(l1, n):
    x = l1.count(n)
    if n in l1:
        l1.remove(n)
        for i in range(x):
            l1.append(n)
        return l1
    else:
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
    num = input("Please enter an integer: ")
    my_list = endNum(l2, num)
    my_list = [int(x) for x in my_list]
    print(my_list, sep=',')
if __name__ == "__main__":
    main()