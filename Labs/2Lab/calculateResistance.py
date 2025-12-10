"""
Ryan Huckaby
Lab #2 (Week Two)
Date Started: 9/10/2025
This code will calculate the resistance, following the users input for the current and voltage.
CITATION - URL: https://byjus.com/resistance-formula/
CITATION - Author: BYJU's
CITATION - Date Written/Posted: 2025
CITATION - Date Accessed: 9/10/25
"""
voltage = int(input("Please input the voltage (without units): "))
current = int(input("Please input the current (without units): "))
resistance = (voltage / current)
print(f"This is the resistance with a current of {current} and a voltage of {voltage}: {resistance}")