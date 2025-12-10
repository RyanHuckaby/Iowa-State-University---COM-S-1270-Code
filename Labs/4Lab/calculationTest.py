"""
Ryan Huckaby
Lab #4 (Week Five)
Date Started: 9/24/2025
Conversion point of multiple previously made codes that the user can access all in one program.
"""
import myFinances
import myOhmsLaw
import myPhysics
import myShapes
def main():
    a = True
    while a:
        program_input = input(str("What would you like to access?\n[F]inances\n[O]hms Law\n[P]hysics\n[S]hapes\n[Q]uit\n: "))
        if program_input not in ["F", "O", "P", "S", "Q"]:
            print("Error invalid input... please try again")
        elif program_input == "Q":
            a = False
        elif program_input == "F":
            specific_function_input = input(str("Which Finance function would you like to use?:\n1. compoundAmount\n2. annualPercentageRate\n: "))
            if specific_function_input == "1":
                print(f"Your compound amount is: {myFinances.compoundAmount()}")
            elif specific_function_input == "2":
                print(f"Your APR is: {myFinances.annualPercentageRate()}")
            else:
                print("Error invalid input... please try again")
        elif program_input == "O":
            specific_function_input = input(str("Which Finance function would you like to use?:\n1. calculateResistance\n2. calculateVoltage\n3. calculateCurrent\n: "))
            if specific_function_input == "1":
                print(f"The resistance is: {myOhmsLaw.calculateResistance()}")
            elif specific_function_input == "2":
                print(f"The voltage is: {myOhmsLaw.calculateVoltage()}")
            elif specific_function_input == "3":
                print(f"The current is: {myOhmsLaw.calculateCurrent()}")
            else:
                print("Error invalid input... please try again")
        elif program_input == "P":
            specific_function_input = input(str("Which Finance function would you like to use?:\n1. distanceSpeedTime\n2. velocityAccelerationTime\n: "))
            if specific_function_input == "1":
                print(f"The distance is: {myPhysics.distanceSpeedTime()}")
            elif specific_function_input == "2":
                print(f"The velocity is: {myPhysics.velocityAccelerationTime()}")
            else:
                print("Error invalid input... please try again")
        elif program_input == "S":
            specific_function_input = input(str("Which Finance function would you like to use?:\n1. areaOfCircle\n2. circleCircumference\n3. areaOfRectangle\n4. rectanglePerimeter\n: "))
            if specific_function_input == "1":
                print(f"The area of your circle is: {myShapes.areaOfCircle()}")
            elif specific_function_input == "2":
                print(f"The circumference of your circle is: {myShapes.circleCircumference()}")
            elif specific_function_input == "3":
                print(f"The area of your rectangle is: {myShapes.areaOfRectangle()}")
            elif specific_function_input == "4":
                print(f"The perimeter of your rectangle is: {myShapes.rectanglePerimeter()}")
            else:
                print("Error invalid input... please try again")
if __name__ == "__main__":
    main()