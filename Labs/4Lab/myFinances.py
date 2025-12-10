"""
Ryan Huckaby
Lab #4 (Week Five)
Date Started: 9/24/2025
Collection of previous code related to Finance
"""
def annualPercentageRate():
    #CITATION - URL: https://www.wallstreetprep.com/knowledge/apr-annual-percentage-rate/
    #CITATION - Author: WallStreetPrep
    #CITATION - Date Written/Posted: 2024
    #CITATION - Date Accessed: 9/17/25
    fees = int(input("Please input the fees (without units): "))
    loan_amount = int(input("Please input the loan amount (without units): "))
    days_in_term = int(input("Please input the days in the term (without units): "))
    interest_charges = int(input("Please input the interest charges (without units): "))
    amount = (((interest_charges + fees) / loan_amount) / days_in_term) * 100
    return amount
def compoundAmount():
    #CITATION - URL: https://byjus.com/maths/compound-interest/
    #CITATION - Author: BYJU's
    #CITATION - Date Written/Posted: 2025
    #CITATION - Date Accessed: 9/17/25
    principal = int(input("Please input the principal amount (without units): "))
    rate = int(input("Please input the interest rate (without the percent sign): "))
    number_compounds = int(input("Please input the number of times the interest compounds in a year (without units): "))
    time = int(input("Please input the time in years (without units): "))
    amount = principal * (1 + (rate/100) / number_compounds)**(number_compounds * time)
    return amount