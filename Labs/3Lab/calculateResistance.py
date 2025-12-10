"""
Ryan Huckaby
Lab #3 (Week Four)
Date Started: 9/17/2025
This is the conversion of a previously made code to calculate the resistance. It now uses the "if" function and the variable "__main__".
"""
def calculateResistance(voltage, current):
    #CITATION - URL: https://byjus.com/resistance-formula/
    #CITATION - Author: BYJU's
    #CITATION - Date Written/Posted: 2025
    #CITATION - Date Accessed: 9/17/25
    return (voltage / current)
def main():
    voltage = int(input("Please input the voltage (without units): "))
    current = int(input("Please input the current (without units): "))
    resistance = calculateResistance(voltage, current)
    print(f"This is the resistance with a current of {current} and a voltage of {voltage}: {resistance}")
if __name__ == "__main__":
    main()