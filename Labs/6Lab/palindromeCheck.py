"""
Ryan Huckaby
Lab #6 (Week Seven)
Date Started: 10/8/2025
This code checks if a string contains a palindrome!
"""
import reverseString as rs
def palindromeCheckV1(n1):
    n3 = n1.lower()
    n2 = rs.reverseStringV4(n3)
    if n2 == n3:
        return (f"{n1} is a palindrome")
    else:
        return (f"{n1} is NOT a palindrome")
    
def palindromeCheckV2(p1):
    p3 = p1.lower()
    p2 = len(p1)
    x = False
    for i in range(p2):
        if p3[i] == p3[(-i)-1]:
            x = True
            continue
        else:
            x = False
            break
    if x:
        return (f"{p1} is a palindrome")
    else:
        return (f"{p1} is NOT a palindrome")

def main():
    string1 = input("Please input what to check if its a palindrome: ")
    print(palindromeCheckV1(string1))
    string2 = input("Please input what to check if its a palindrome: ")
    print(palindromeCheckV2(string2))

if __name__ == "__main__":
    main()