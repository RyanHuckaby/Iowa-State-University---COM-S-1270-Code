"""
Ryan Huckaby
Lab #2 (Week Two)
Date Started: 9/10/2025
This code will calculate the final velocity, following the users input for the initial velocity, acceleration, and time.
CITATION - URL: https://www.calculatorsoup.com/calculators/physics/velocity_a_t.php
CITATION - Author: Calculatorsoup
CITATION - Date Written/Posted: 2025
CITATION - Date Accessed: 9/10/25
"""
initial_velocity = int(input("Please input the velocity (meters per second): "))
acceleration = int(input("Please input the acceleration (meters per second sqrd): "))
time = int(input("Please input the time (seconds): "))
final_velocity = initial_velocity + (acceleration * time)
print(f"The resulting final velocity after {time}s at an initial velocity of {initial_velocity} meters per second and an acceleration of {acceleration} meters per second sqrd is: {final_velocity} meters per second")