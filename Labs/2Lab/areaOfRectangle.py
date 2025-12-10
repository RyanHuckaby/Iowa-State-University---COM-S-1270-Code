"""
Ryan Huckaby
Lab #2 (Week Two)
Date Started: 9/10/2025
This code will calculate the area of a rectangle, following the users input for the base and height.
CITATION - URL: https://math.libretexts.org/Bookshelves/Geometry/Elementary_College_Geometry_(Africk)/06%3A_Area_and_Perimeter/6.01%3A_The_Area_of_a_Rectangle_and_Square
CITATION - Author: Henry Africk
CITATION - Date Written/Posted: 2025
CITATION - Date Accessed: 9/10/25
"""
base = int(input("Please input the base of your rectangle (without units): "))
height = int(input("Please input the height of your rectangle (without units): "))
area = (base * height)
print(f"This is the area of your rectangle, with a base of {base} and a height of {height}: {area}")