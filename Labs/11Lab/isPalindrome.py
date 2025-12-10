"""
Ryan Huckaby
Lab #11 (Week Fifteen)
Date Started: 12/3/2025
Description: Uses iteration and recursion to check if strings are palindromes.
"""

def isPalindromeIterative(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def isPalindromeRecursive(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return isPalindromeRecursive(s[1:-1])


def main():
    text = input("Enter text: ")

    print(isPalindromeIterative(text))
    print(isPalindromeRecursive(text))


if __name__ == "__main__":
    main()