"""
Ryan Huckaby
Lab #2 (Week Two)
Date Started: 9/10/2025
This code will calculate the apr (Annual Percentage Rate), following the users input for the fees, loan amount, days in the term, and interest charges.
CITATION - URL: https://www.wallstreetprep.com/knowledge/apr-annual-percentage-rate/
CITATION - Author: WallStreetPrep
CITATION - Date Written/Posted: 2024
CITATION - Date Accessed: 9/10/25
"""
fees = int(input("Please input the fees (without units): "))
loan_amount = int(input("Please input the loan amount (without units): "))
days_in_term = int(input("Please input the days in the term (without units): "))
interest_charges = int(input("Please input the interest charges (without units): "))
apr = (((interest_charges + fees) / loan_amount) / days_in_term) * 100
print(f"This is the apr on a ${loan_amount} loan with ${fees} fees, {days_in_term} days in term, and {interest_charges} interest: {apr}")