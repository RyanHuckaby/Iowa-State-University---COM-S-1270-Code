"""
Ryan Huckaby
Lab #2 (Week Two)
Date Started: 9/10/2025
This code will calculate the compound interest (accrued amount), following the users input for the principal amount, interest rate, 
the number of times the interest compounds in a year, and a time in years.
CITATION - URL: https://byjus.com/maths/compound-interest/
CITATION - Author: BYJU's
CITATION - Date Written/Posted: 2025
CITATION - Date Accessed: 9/10/25
"""
principal = int(input("Please input the principal amount (without units): "))
rate = int(input("Please input the interest rate (without the percent sign): "))
number_compounds = int(input("Please input the number of times the interest compounds in a year (without units): "))
time = int(input("Please input the time in years (without units): "))
accrued_amount = principal * (1 + (rate/100) / number_compounds)**(number_compounds * time)
print(f"This is the accrued amount on a ${principal} principal amount with {rate}% interest rate, {number_compounds}  number of compounds in a year, and in {time} years: {accrued_amount}")