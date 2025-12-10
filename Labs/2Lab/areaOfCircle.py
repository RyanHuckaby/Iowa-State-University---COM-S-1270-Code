"""
Ryan Huckaby
Lab #2 (Week Two)
Date Started: 9/10/2025
This code will calculate the area of a circle, following the users input for the radius.
CITATION - URL: https://www.cuemath.com/geometry/area-of-a-circle/
CITATION - Author: CueMath
CITATION - Date Written/Posted: 2025
CITATION - Date Accessed: 9/10/25
"""
import math
radius = int(input("Please input the radius of your circle (without units): "))
area = math.pi * (radius ** 2)
print(f"This is the area of your circle with a radius of {radius}: {area}")