"""
Ryan Huckaby
Lab #3 (Week Four)
Date Started: 9/17/2025
This is the conversion of a previous code to calculate the area of a rectange. It now uses the "if" function and the variable "__main__". 
"""
def areaOfRectangle(base, height):
    #CITATION - URL: https://math.libretexts.org/Bookshelves/Geometry/Elementary_College_Geometry_(Africk)/06%3A_Area_and_Perimeter/6.01%3A_The_Area_of_a_Rectangle_and_Square
    #CITATION - Author: Henry Africk
    #CITATION - Date Written/Posted: 2025
    #CITATION - Date Accessed: 9/17/2025
    return base * height
def main():
    base = int(input("Please input the base of your rectangle (without units): "))
    height = int(input("Please input the height of your rectangle (without units): "))
    area = areaOfRectangle(base, height)
    print(f"The area of a rectangle with a base of {base} and height of {height} is: {area}")
if __name__ == "__main__":
    main()