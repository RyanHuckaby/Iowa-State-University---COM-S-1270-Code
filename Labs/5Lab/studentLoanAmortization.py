"""
Ryan Huckaby
Lab #5 (Week Six)
Date Started: 10/1/2025
This code creates an Amortization table.
"""
def studentLoanAmortization(p, m, n):
    if m > 0:
        payment = (p * m) / (1 - (1 + m) ** -n)
    else:
        payment = p / n
    balance = p
    print(f'{"Period":<11}{"Total Payment Due":<22}{"Computed Interest":<22}{"Principal Due":<18}{"Principal Balance":<22}')
    for period in range(1, n+1):
        interest = balance * m
        principalPaid = payment - interest
        balance -= principalPaid
        if period == n:
            balance = 0
        print(f"{period:<11}{payment:<22.2f}{interest:<22.2f}{principalPaid:<18.2f}{balance:<22.2f}")
def main():
    principal = float(input("Please Input the Principal: "))
    yearlyInterestRate = float(input("Please Input the Yearly Interest: "))
    numberOfYears = int(input("Please Input the Number of Years: "))
    monthlyRate = yearlyInterestRate / 100 / 12 if yearlyInterestRate > 0 else 0
    numberOfPayments = numberOfYears * 12
    studentLoanAmortization(principal, monthlyRate, numberOfPayments)
if __name__ == "__main__":
    main()