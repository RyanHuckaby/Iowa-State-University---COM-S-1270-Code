"""
Ryan Huckaby
Lab #4 (Week Five)
Date Started: 9/24/2025
This code is a modification of a previous code to draw a tridecagon, now it draws multiple of them depending on the user's input for how many and how far apart.
specified by the user.
"""
import turtle
def tridecagonTurtle(s, t):
    #CITATION - URL: https://en.wikipedia.org/wiki/Tridecagon
    #CITATION - Author: Wikipedia
    #CITATION - Date Written/Posted: 2025
    #CITATION - Date Accessed: 9/17/25
    t.penup()
    t.width(5)
    t.left(27.6923)
    t.pendown()
    for i in range(1, 14):
        t.backward(s)
        t.right(27.6923)
def main():
    t = turtle.Turtle()
    s = 10 * (int(input("Please choose the length of the sides: ")))
    x = int(input("What x coordinate would you like the tridecagon to start at?: "))
    y = int(input("What y coordinate would you like the tridecagon to start at?: "))
    nr = int(input("How many tridecagons do you want to draw?: "))
    sr = 10 * int(input("How much space should be between the tridecagons?: "))
    drawMultipleTridecagons(s, x, y, nr, sr, t)
def drawMultipleTridecagons(s, x, y, nr, sr, t):
    t.setposition(x,y)
    for i in range(nr):
        tridecagonTurtle(s, t)
        t.penup()
        t.right(27.6923)
        t.forward(sr)
        t.pendown()
    wn = turtle.Screen()
    wn.exitonclick()
if __name__ == "__main__":
    main()