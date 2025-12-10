"""
Ryan Huckaby
Lab #4 (Week Five)
Date Started: 9/24/2025
Collection of previous code related to Shapes
"""
import math
def areaOfCircle():
    #CITATION - URL: https://www.cuemath.com/geometry/area-of-a-circle/
    #CITATION - Author: CueMath
    #CITATION - Date Written/Posted: 2025
    #CITATION - Date Accessed: 9/17/25
    radius = int(input("Please input the radius of your circle (without units): "))
    amount = math.pi * (radius ** 2)
    return amount
def circleCircumference():
    #CITATION - URL: https://byjus.com/maths/circumference-of-a-circle/
    #CITATION - Author: BYJU's
    #CITATION - Date Written/Posted: 2020
    #CITATION - Date Accessed: 9/17/25
    radius = int(input("Please input the radius of your circle (without units): "))
    amount = 2 * math.pi * radius
    return amount
def areaOfRectangle():
    #CITATION - URL: https://math.libretexts.org/Bookshelves/Geometry/Elementary_College_Geometry_(Africk)/06%3A_Area_and_Perimeter/6.01%3A_The_Area_of_a_Rectangle_and_Square
    #CITATION - Author: Henry Africk
    #CITATION - Date Written/Posted: 2025
    #CITATION - Date Accessed: 9/17/2025
    base = int(input("Please input the base of your rectangle (without units): "))
    height = int(input("Please input the height of your rectangle (without units): "))
    amount = base * height
    return amount
def rectanglePerimeter():
    #CITATION - URL: https://byjus.com/maths/perimeter-of-rectangle/
    #CITATION - Author: BYJU's
    #CITATION - Date Written/Posted: 2020
    #CITATION - Date Accessed: 9/17/25
    base = int(input("Please input the base of your rectangle (without units): "))
    height = int(input("Please input the height of your rectangle (without units): "))
    amount = 2 * (base + height)
    return amount