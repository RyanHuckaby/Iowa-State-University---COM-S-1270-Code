"""
Ryan Huckaby
Lab #11 (Week Fifteen)
Date Started: 12/3/2025
Description: Uses iteration and recursion to reverse strings.
"""

def reverseIterative(s):
    result = ""
    i = len(s) - 1
    while i >= 0:
        result += s[i]
        i -= 1
    return result


def reverseRecursive(s):
    if len(s) <= 1:
        return s
    return reverseRecursive(s[1:]) + s[0]


def main():
    text = input("Enter text: ")

    print(reverseIterative(text))
    print(reverseRecursive(text))


if __name__ == "__main__":
    main()