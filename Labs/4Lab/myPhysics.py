"""
Ryan Huckaby
Lab #4 (Week Five)
Date Started: 9/24/2025
Collection of previous code related to Physics
"""
def distanceSpeedTime():
    #CITATION - URL: https://byjus.com/distance-speed-time-formula/
    #CITATION - Author: BYJU's
    #CITATION - Date Written/Posted: 2020
    #CITATION - Date Accessed: 9/17/25
    speed = int(input("Please input the speed (meters per second): "))
    time = int(input("Please input the time (seconds): "))
    amount = (speed * time)
    return amount
def velocityAccelerationTime():
    #CITATION - URL: https://www.calculatorsoup.com/calculators/physics/velocity_a_t.php
    #CITATION - Author: Calculatorsoup
    #CITATION - Date Written/Posted: 2025
    #CITATION - Date Accessed: 9/17/25
    initial_velocity = int(input("Please input the velocity (meters per second): "))
    acceleration = int(input("Please input the acceleration (meters per second sqrd): "))
    time = int(input("Please input the time (seconds): "))
    amount = initial_velocity + (acceleration * time)
    return amount