"""
Ryan Huckaby
Lab #6 (Week Seven)
Date Started: 10/8/2025
This code reverses strings in multiple different ways
"""
def reverseStringV1(s1):
    s2 = s1[::-1]
    return s2

def reverseStringV2(r1):
    r2 = reversed(r1)
    r3 = "".join(r2)
    return r3

def reverseStringV3(b1):
    b2 = ""
    for i in range(len(b1) -1, -1, -1):
        b2 += b1[i]
    return b2

def reverseStringV4(n1):
    n2 = ""
    for i in n1:
        n2 = i + n2
    return n2

def reverseStringV5(c1):
    c2 = ""
    i = len(c1) -1
    while i >= 0:
        c2 += c1[i]
        i -= 1
    return c2        

def main():
    string1 = input("What phrase would you like to be reversed? ")
    print(reverseStringV1(string1))
    string2 = input("What phrase would you like to be reversed? ")
    print(reverseStringV2(string2))
    string3 = input("What phrase would you like to be reversed? ")
    print(reverseStringV3(string3))
    string4 = input("What phrase would you like to be reversed? ")
    print(reverseStringV4(string4))
    string5 = input("What phrase would you like to be reversed? ")
    print(reverseStringV5(string5))
    
if __name__ == "__main__":
    main()