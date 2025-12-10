"""
Ryan Huckaby
Lab #3 (Week Four)
Date Started: 9/17/2025
This code uses inputs from the user to find the sqaure root of a number using iterations.
"""
def sqrtIter(x, iterations):
    #CITATION - URL: https://www.cuemath.com/algebra/square-root-of-2/
    #CITATION - Author: Cuemath
    #CITATION - Date Written/Posted: 2025
    #CITATION - Date Accessed: 9/17/25
    y = 1
    for i in range(0, iterations):
        y_0 = y
        y = (x + y_0) / 2
        y = ((x / y_0) + y_0) / 2
    return float(y)
def main():
    int1 = int(input("Please input an integer you want to take the squre root of: "))
    iterations = int(input("Please input the iteration amount: "))  
    print(f"The square root of {int1} is: {sqrtIter(int1, iterations)}")
if __name__ == "__main__":
    main()