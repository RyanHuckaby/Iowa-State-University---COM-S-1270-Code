"""
Ryan Huckaby
Lab #3 (Week Four)
Date Started: 9/17/2025
This is the conversion of a previous code to calculate the area of a circle. It now uses the "if" function and the variable "__main__".
"""
import math
def areaOfCircle(radius):
    #CITATION - URL: https://www.cuemath.com/geometry/area-of-a-circle/
    #CITATION - Author: CueMath
    #CITATION - Date Written/Posted: 2025
    #CITATION - Date Accessed: 9/17/25
    return math.pi * (radius ** 2)
def main():
    radius = int(input("Please input the radius of your circle (without units): "))
    area = areaOfCircle(radius)
    print(f"This is the area of your circle with a radius of {radius}: {area}")
if __name__ == "__main__":
    main()