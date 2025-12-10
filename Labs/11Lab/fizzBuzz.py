"""
Ryan Huckaby
Lab #11 (Week Fifteen)
Date Started: 12/3/2025
Description: Multiple ways to play the game FizzBuzz!
"""

#CITATION - URL: https://www.enjoyalgorithms.com/blog/fizz-buzz-problem
#CITATION - Author: Enjoy Algorithms
#CITATION - Date Accessed: 12/3/2025

def fizzBuzzModulus(n):
    result = []
    for i in range(1, n + 1):
        word = ""
        if i % 3 == 0:
            word += "Fizz"
        if i % 5 == 0:
            word += "Buzz"
        if i % 7 == 0:
            word += "Bazz"
        if word == "":
            word = str(i)
        result.append(word)
    return result


def fizzBuzzDict(n):
    result = []
    rules = {3: "Fizz", 5: "Buzz", 7: "Bazz"}

    for i in range(1, n + 1):
        word = ""
        for key in rules:
            if i % key == 0:
                word += rules[key]
        if word == "":
            word = str(i)
        result.append(word)

    return result


def main():
    n = int(input("Enter an integer: "))

    print(fizzBuzzModulus(n))
    print(fizzBuzzDict(n))


if __name__ == "__main__":
    main()