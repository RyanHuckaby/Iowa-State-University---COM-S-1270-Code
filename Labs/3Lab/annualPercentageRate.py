"""
Ryan Huckaby
Lab #3 (Week Four)
Date Started: 9/17/2025
This is the conversion of a previously made code to calculate the apr (Annual Percentage Rate). It now uses the "if" function and the variable "__main__".
"""
def annualPercentageRate(fees, loan_amount, days_in_term, interest_charges):
    #CITATION - URL: https://www.wallstreetprep.com/knowledge/apr-annual-percentage-rate/
    #CITATION - Author: WallStreetPrep
    #CITATION - Date Written/Posted: 2024
    #CITATION - Date Accessed: 9/17/25
    return (((interest_charges + fees) / loan_amount) / days_in_term) * 100
def main():
    fees = int(input("Please input the fees (without units): "))
    loan_amount = int(input("Please input the loan amount (without units): "))
    days_in_term = int(input("Please input the days in the term (without units): "))
    interest_charges = int(input("Please input the interest charges (without units): "))
    apr = annualPercentageRate(fees, loan_amount, days_in_term, interest_charges)
    print(f"This is the apr on a ${loan_amount} loan with ${fees} fees, {days_in_term} days in term, and {interest_charges} interest: {apr}")
if __name__ == "__main__":
    main()