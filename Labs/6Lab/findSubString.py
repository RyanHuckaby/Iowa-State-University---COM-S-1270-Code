"""
Ryan Huckaby
Lab #6 (Week Seven)
Date Started: 10/8/2025
This code checks if a substring is in a string and then returns the index if it is present!
"""
def findSubStringV1(n1, n2):
    index = n1.find(n2)
    return index

def findSubStringV2(n1, n2):
    if n2 in n1:
        return n1.index(n2)
    else:
        return -1

def findSubStringV3(n1, n2):
    l = len(n1)
    s = len(n2)
    for i in range((l - s) + 1):
        x = True
        for k in range(s):
            if n1[i+k] != n2[k]:
                x = False
                break
        if x:
            return i
    return -1
    

def main():
    print("Method 1\n")
    string1_1 = input("Please input your first phrase: ")
    string1_2 = input("What phrase would you like to find in the previous phrase?: ")
    if findSubStringV1(string1_1, string1_2) != -1:
        print(f"\n'{string1_2}' is in '{string1_1}' at index: {findSubStringV1(string1_1, string1_2)}")
    else:
        print(f"\n'{string1_2}' is NOT in '{string1_1}'")
    print("\nMethod 2\n")
    string2_1 = input("Please input your first phrase: ")
    string2_2 = input("What phrase would you like to find in the previous phrase?: ")
    if findSubStringV2(string2_1, string2_2) != -1:
        print(f"\n'{string2_2}' is in '{string2_1}' at index: {findSubStringV2(string2_1, string2_2)}")
    else:
        print(f"\n'{string2_2}' is NOT in '{string2_1}'")
    print("\nMethod 3\n")
    string3_1 = input("Please input your first phrase: ")
    string3_2 = input("What phrase would you like to find in the previous phrase?: ")
    if findSubStringV3(string3_1, string3_2) != -1:
        print(f"\n'{string3_2}' is in '{string3_1}' at index: {findSubStringV3(string3_1, string3_2)}")
    else:
        print(f"\n'{string3_2}' is NOT in '{string3_1}'")
    
if __name__ == "__main__":
    main()