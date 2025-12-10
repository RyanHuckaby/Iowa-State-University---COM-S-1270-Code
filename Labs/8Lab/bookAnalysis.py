"""
Ryan Huckaby
Lab #8 (Week Ten)
Date Started: 10/29/2025
This code reads through a book and counts how many words there are as well as how many times each one appears.
"""
def outputAnalysis(count, name):
    keys = list(count.keys())
    keys.sort()
    
    # save the word count analysis to a file
    with open(f'{name}_analysis.txt', 'w') as file:

        for word in keys:
            file.write(word + " " + str(count[word]))
            file.write('\n')
            
def analyzeBook(name):
    with open(f'{name}.txt', 'r') as file:

        count = {}

        for line in file:

            for word in line.split():
                # remove punctuation
                word = word.replace('_', '').replace('"', '').replace(',', '').replace('.', '')
                word = word.replace('-', '').replace('?', '').replace('!', '').replace("'", "")
                word = word.replace('(', '').replace(')', '').replace(':', '').replace('[', '')
                word = word.replace(']', '').replace(';', '')

                # ignore case
                word = word.lower()

                # ignore numbers
                if word.isalpha():
                    if word in count:
                        count[word] = count[word] + 1
                    else:
                        count[word] = 1
    return count

def main():
    fileName = input("What is the name of the file? ")
    output = analyzeBook(fileName)
    outputAnalysis(output, fileName)

if __name__ == "__main__":
    main()