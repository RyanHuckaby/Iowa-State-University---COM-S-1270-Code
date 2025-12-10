"""
Ryan Huckaby
Lab #3 (Week Four)
Date Started: 9/17/2025
This is the conversion of a previously made code to calculate the distance traveled. It now uses the "if" function and the variable "__main__".
"""
def distanceSpeedTime(speed, time):
    #CITATION - URL: https://byjus.com/distance-speed-time-formula/
    #CITATION - Author: BYJU's
    #CITATION - Date Written/Posted: 2020
    #CITATION - Date Accessed: 9/17/25
    return (speed * time)
def main():
    speed = int(input("Please input the speed (meters per second): "))
    time = int(input("Please input the time (seconds): "))
    distance = distanceSpeedTime(speed, time)
    print(f"The resulting distance after {time}s at {speed} meters per second is: {distance} meters")
if __name__ == "__main__":
    main()