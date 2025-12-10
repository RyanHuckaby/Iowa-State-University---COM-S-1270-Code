"""
Ryan Huckaby
Lab #7 (Week Eight)
Date Started: 10/15/2025
This code finds basic statistical information based on random number lists
"""
from random import randint
def generateInput():
    l1 = []
    for i in range(randint(200, 501)):
        l1.append(randint(1, 2000))
    return l1
def findMean(l1):
    #CITATION - URL: https://byjus.com/maths/mean/
    #CITATION - Author: BYJU's
    #CITATION - Date Written/Posted: 2025
    #CITATION - Date Accessed: 10/15/25
    #CITATION - "The mean is one of the measures of central tendency, 
    #            apart from the mode and median. Mean is nothing but 
    #            the average of the given set of values."
    num = 0
    for i in range(len(l1)):
        num += int(l1[i])
        return num
    mean = float(num / len(l1))
    return mean
def findMedian(l1):
    #CITATION - URL: https://byjus.com/maths/median/
    #CITATION - Author: BYJU's
    #CITATION - Date Written/Posted: 2025
    #CITATION - Date Accessed: 10/15/25
    #CITATION - "Median, in statistics, is the middle value of the 
    #            given list of data when arranged in an order."
    lenl1 = len(l1)
    l1.sort()
    if lenl1 % 2 == 0: #even length (2 middle)
        mid = int(lenl1/2) # finds the position of both middle
        median = ((l1[(mid-1)]) + (l1[(mid)])) / 2
        return median
    elif lenl1 % 2 != 0: #odd length (1 middle)
        mid = int((lenl1/2) + (1-(lenl1 % 2))) #find position of the middle
        median = l1[mid]
        return median
    else:
        return
def main():
    l2 = generateInput()
    mean = findMean(l2)
    median = findMedian(l2)
    print(f"Mean: {mean} Median: {median}")
if __name__ == "__main__":
    main()