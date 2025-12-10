"""
Ryan Huckaby
Lab #3 (Week Four)
Date Started: 9/17/2025
This is the conversion of a previously made code to calculate the final velocity. It now uses the "if" function and the variable "__main__".
"""
def velocityAccelerationTime(initial_velocity, acceleration, time):
    #CITATION - URL: https://www.calculatorsoup.com/calculators/physics/velocity_a_t.php
    #CITATION - Author: Calculatorsoup
    #CITATION - Date Written/Posted: 2025
    #CITATION - Date Accessed: 9/17/25
    return initial_velocity + (acceleration * time)
def main():
    initial_velocity = int(input("Please input the velocity (meters per second): "))
    acceleration = int(input("Please input the acceleration (meters per second sqrd): "))
    time = int(input("Please input the time (seconds): "))
    final_velocity = velocityAccelerationTime(initial_velocity, acceleration, time)
    print(f"The resulting final velocity after {time}s at an initial velocity of {initial_velocity} meters per second and an acceleration of {acceleration} meters per second sqrd is: {final_velocity} meters per second")
if __name__ == "__main__":
    main()