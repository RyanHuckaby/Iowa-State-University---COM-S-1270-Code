"""
Ryan Huckaby
Lab #2 (Week Two)
Date Started: 9/10/2025
This code will calculate the area of a perimeter, following the users input for the base and height.
CITATION - URL: https://byjus.com/maths/perimeter-of-rectangle/
CITATION - Author: BYJU's
CITATION - Date Written/Posted: 2020
CITATION - Date Accessed: 9/10/25
"""
base = int(input("Please input the base of your rectangle (without units): "))
height = int(input("Please input the height of your rectangle (without units): "))
perimeter = 2 * (base + height)
print(f"This is the perimeter of your rectangle when it has a base of {base} and a height of {height}: {perimeter}")