"""
Ryan Huckaby
Lab #3 (Week Four)
Date Started: 9/17/2025
This is the conversion of a previously made code to calculate the circumference of a circle. It now uses the "if" function and the variable "__main__".
"""
import math
def circleCircumference(radius):
    #CITATION - URL: https://byjus.com/maths/circumference-of-a-circle/
    #CITATION - Author: BYJU's
    #CITATION - Date Written/Posted: 2020
    #CITATION - Date Accessed: 9/17/25
    return 2 * math.pi * radius
def main():
    radius = int(input("Please input the radius of your circle (without units): "))
    circumference = circleCircumference(radius)
    print(f"This is the circumference of your circle with a radius {radius}: {circumference}")
if __name__ == "__main__":
    main()