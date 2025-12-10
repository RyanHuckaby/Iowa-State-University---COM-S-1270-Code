"""
Ryan Huckaby
Lab #3 (Week Four)
Date Started: 9/17/2025
This is the conversion of a previously made code to calculate the area of a perimeter. It now uses the "if" function and the variable "__main__".
"""
def rectanglePerimeter(base, height):
    #CITATION - URL: https://byjus.com/maths/perimeter-of-rectangle/
    #CITATION - Author: BYJU's
    #CITATION - Date Written/Posted: 2020
    #CITATION - Date Accessed: 9/17/25
    return 2 * (base + height)
def main():
    base = int(input("Please input the base of your rectangle (without units): "))
    height = int(input("Please input the height of your rectangle (without units): "))
    perimeter = rectanglePerimeter(base, height)
    print(f"This is the perimeter of your rectangle when it has a base of {base} and a height of {height}: {perimeter}")
if __name__ == "__main__":
    main()