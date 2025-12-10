"""
Ryan Huckaby
Date Started: 9/6/2025
Assignment #1
In this code it is going to take inputs from the individual
and use those inputs in funny short stories -- Zany Texts!
"""
print("Zany Texts!")
print()
print("By: Ryan Huckaby")
print("[COM S 1270 2]")
print()
#First Zany Text
print("Zany Text #1")
name = input("Choose your favorite name: ")
pet = input("If you could have any animal, what would it be?: ")
pet_name = input("What would you name it?: ")
verb = input("Now choose a verb!: ")
print()
def first_text(name,pet,pet_name,verb):
    return"How are you doing today, " + name + "? I hope you and your " + pet + ", " + pet_name + ", are having a wonderful " + verb + " together!"
print(first_text(name,pet,pet_name,verb))
print()
#Second Zany Text
print("Zany Text #2")
print(f"Long time no see {input('What is your name?: ')}! How's {input('Now what is your favorite class you are taking this semester?: ')} going for you this semester? I heard you got a {int(input('Pick a random number from 1-100: '))}% in it...")
print()
#Third Zany Text
print("Zany Text #3")
Third_Number = (10 * float(input("How would you rate the seasons dining hall on a scale of 1-10?: ")))
print()
if Third_Number >= 75:
    print("Happy to hear you've enjoyed your ISU dining experience.")
elif 40 < Third_Number < 75:
     print("I agree! Those late night hours really feed the cravings.")
else:
    print("Whatever you do, totally stay away from UDCC, the food is TERRIBLE...")
print()
#Fourth Zany Text
print("Zany Text #4")
sound = input("What's your least favorite sound to hear while sleeping?: ")
print()
print((sound + ", ") * 3 + "...and you wonder why I couldn't sleep last night!")