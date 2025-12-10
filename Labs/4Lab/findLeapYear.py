"""
Ryan Huckaby
Lab #4 (Week Five)
Date Started: 9/24/2025
This code finds if a specified year is a leap year or not.
"""
def findLeapYear(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True 
    else:
        return False
def main():
    year = int(input("Please enter a year: "))
    if findLeapYear(year) == True:
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is NOT a leap year.")
if __name__ == "__main__":
    main()