"""
Ryan Huckaby
Lab #2 (Week Two)
Date Started: 9/10/2025
This code will calculate the distance traveled, following the users input for the speed and time.
CITATION - URL: https://byjus.com/distance-speed-time-formula/
CITATION - Author: BYJU's
CITATION - Date Written/Posted: 2020
CITATION - Date Accessed: 9/10/25
"""
speed = int(input("Please input the speed (meters per second): "))
time = int(input("Please input the time (seconds): "))
distance = (speed * time)
print(f"The resulting distance after {time}s at {speed} meters per second is: {distance} meters")