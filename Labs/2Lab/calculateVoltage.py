"""
Ryan Huckaby
Lab #2 (Week Two)
Date Started: 9/10/2025
This code will calculate the voltage, following the users input for the current and resistance.
CITATION - URL: https://byjus.com/physics/unit-of-voltage/
CITATION - Author: BYJU's
CITATION - Date Written/Posted: 2025
CITATION - Date Accessed: 9/10/25
"""
resistance = int(input("Please input the resistance (without units): "))
current = int(input("Please input the current (without units): "))
voltage = (current * resistance)
print(f"This is the voltage with a current of {current} and a reistance of {resistance}: {voltage}")