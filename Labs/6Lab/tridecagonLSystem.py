"""
Ryan Huckaby
Lab #6 (Week Seven)
Date Started: 10/8/2025
This code changes the Runestone Example to include a new tridecagon drawing command "T" and random teleport command "P".
"""
from drawMultipleTridecagons import drawMultipleTridecagons; import turtle, random as r
#CITATION - URL: https://runestone.academy/ns/books/published/thinkcspy/Strings/TurtlesandStringsandLSystems.html
#CITATION - Author: Runestone
#CITATION - Date Written/Posted: 2025
#CITATION - Date Accessed: 10/8/25
def createLSystem(numIters,axiom):
    startString = axiom
    endString = ""
    for i in range(numIters):
        endString = processString(startString)
        startString = endString

    return endString

def processString(oldStr):
    newstr = ""
    for ch in oldStr:
        newstr = newstr + applyRules(ch)

    return newstr

def applyRules(ch):
    if ch == 'F':
        return 'F-F++F-F'
    elif ch == 'T':
        return 'T--F+F+P++FF'
    elif ch == 'P':
        return 'P--P++T+-F--F-F'
    else:
        return ch

def drawLsystem(aTurtle, instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)
        elif cmd == "T":
            x_coordinate = aTurtle.xcor()
            y_coordinate = aTurtle.ycor()
            drawMultipleTridecagons(r.randint(10, 100) ,x_coordinate, y_coordinate, 1, 0, aTurtle)
        elif cmd == "P":
            aTurtle.penup()
            aTurtle.goto(r.randint(1,100) ,r.randint(1,100))
            aTurtle.pendown()
def main():
    inst = createLSystem(2, "FTP")   # create the string
    print(inst)
    t = turtle.Turtle()            # create the turtle
    wn = turtle.Screen()

    t.up()
    t.back(200)
    t.down()
    t.speed(10)
    drawLsystem(t, inst, r.randint(0, 180), r.randint(25, 50))   # draw the picture
                                  # angle 60, segment length 5
    wn.exitonclick()

if __name__ == "__main__":
    main()