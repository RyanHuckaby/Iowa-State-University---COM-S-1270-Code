"""
Ryan Huckaby
Lab #8 (Week Ten)
Date Started: 10/29/2025
This code swaps words in a sentence with something random!
"""
from random import choice
def main():
    sentence = input("Please input a sentence: ")
    words = sentence.split()
    word_dict = {}
    for n in set(words):
        word_dict[n] = choice(words)
    print(word_dict)
    new_sentence = [word_dict[n] for n in words]
    print(" ".join(new_sentence))
if __name__ == "__main__":
    main()