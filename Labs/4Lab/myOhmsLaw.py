"""
Ryan Huckaby
Lab #4 (Week Five)
Date Started: 9/24/2025
Collection of previous code related to Ohms Law(Electricity)
"""
def calculateResistance():
    #CITATION - URL: https://byjus.com/resistance-formula/
    #CITATION - Author: BYJU's
    #CITATION - Date Written/Posted: 2025
    #CITATION - Date Accessed: 9/17/25
    voltage = int(input("Please input the voltage (without units): "))
    current = int(input("Please input the current (without units): "))
    amount = (voltage / current)
    return amount
def calculateVoltage():
    #CITATION - URL: https://byjus.com/physics/unit-of-voltage/
    #CITATION - Author: BYJU's
    #CITATION - Date Written/Posted: 2025
    #CITATION - Date Accessed: 9/17/25
    resistance = int(input("Please input the resistance (without units): "))
    current = int(input("Please input the current (without units): "))
    amount = (current * resistance)
    return amount
def calculateCurrent():
    #CITATION - URL: https://www.cuemath.com/current-formula/
    #CITATION - Author: Cuemath
    #CITATION - Date Written/Posted: 2025
    #CITATION - Date Accessed: 9/17/25
    voltage = int(input("Please input the voltage (without units): "))
    resistance = int(input("Please input the resistance (without units): "))
    amount = (voltage / resistance)
    return amount