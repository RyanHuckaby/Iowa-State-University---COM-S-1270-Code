"""
Ryan Huckaby
Lab #3 (Week Four)
Date Started: 9/17/2025
This is the conversion of a previously made code to calculate the compound interest (accrued amount). It now uses the "if" function and the variable "__main__".
"""
def compoundAmount(principal, rate, number_compounds, time):
    #CITATION - URL: https://byjus.com/maths/compound-interest/
    #CITATION - Author: BYJU's
    #CITATION - Date Written/Posted: 2025
    #CITATION - Date Accessed: 9/17/25
    return principal * (1 + (rate/100) / number_compounds)**(number_compounds * time)
def main():
    principal = int(input("Please input the principal amount (without units): "))
    rate = int(input("Please input the interest rate (without the percent sign): "))
    number_compounds = int(input("Please input the number of times the interest compounds in a year (without units): "))
    time = int(input("Please input the time in years (without units): "))
    accrued_amount = compoundAmount(principal, rate, number_compounds, time)
    print(f"This is the accrued amount on a ${principal} principal amount with {rate}% interest rate, {number_compounds}  number of compounds in a year, and in {time} years: {accrued_amount}")
if __name__ == "__main__":
    main()