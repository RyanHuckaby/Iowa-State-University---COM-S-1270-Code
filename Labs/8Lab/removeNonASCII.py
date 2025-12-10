"""
Ryan Huckaby
Lab #8 (Week Ten)
Date Started: 10/29/2025
This code reads through a text file and then removes non ASCII characters to a new file.
"""
def removeNonASCII(name):
    clean = ""
    for ch in name:
        if ord(ch) <= 127:
            clean += ch
        else:
            continue
    return clean
def readFile(name):
    with open(name, "r") as file:
        content = file.read()
        file.close()
    return content
def main():
    x = readFile("testFile.txt")
    cleanFile = removeNonASCII(x)
    with open("testFile_clean.txt", "w") as file:
        file.write(cleanFile)
        file.close()
if __name__ == "__main__":
    main()