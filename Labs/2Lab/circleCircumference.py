"""
Ryan Huckaby
Lab #2 (Week Two)
Date Started: 9/10/2025
This code will calculate the circumference of a circle, following the users input for the radius.
CITATION - URL: https://byjus.com/maths/circumference-of-a-circle/
CITATION - Author: BYJU's
CITATION - Date Written/Posted: 2020
CITATION - Date Accessed: 9/10/25
"""
import math
radius = int(input("Please input the radius of your circle (without units): "))
circumference = 2 * math.pi * radius
print(f"This is the circumference of your circle with a radius {radius}: {circumference}")