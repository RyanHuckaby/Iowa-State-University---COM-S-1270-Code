"""
Ryan Huckaby
Lab #3 (Week Four)
Date Started: 9/17/2025
This is the conversion of a previously made code to calculate the voltage. It now uses the "if" function and the variable "__main__".
"""
def calculateVoltage(resistance, current):
    #CITATION - URL: https://byjus.com/physics/unit-of-voltage/
    #CITATION - Author: BYJU's
    #CITATION - Date Written/Posted: 2025
    #CITATION - Date Accessed: 9/17/25
    return (current * resistance)
def main():
    resistance = int(input("Please input the resistance (without units): "))
    current = int(input("Please input the current (without units): "))
    voltage = calculateVoltage(resistance, current)
    print(f"This is the voltage with a current of {current} and a reistance of {resistance}: {voltage}")
if __name__ == "__main__":
    main()