"""
Ryan Huckaby
Lab #3 (Week Four)
Date Started: 9/17/2025
This code uses inputs from the user (s, x, y, and t as parameters) to draw a shape called a regular tridecagon at the location and at the size
specified by the user.
"""
import turtle
def tridecagonTurtle(s, x, y, t):
    #CITATION - URL: https://en.wikipedia.org/wiki/Tridecagon
    #CITATION - Author: Wikipedia
    #CITATION - Date Written/Posted: 2025
    #CITATION - Date Accessed: 9/17/25
    wn = turtle.Screen()
    t.screen.title("Regular Tridecagon")
    t.penup()
    t.width(5)
    t.setposition(x,y)
    t.left(27.6923)
    t.pendown()
    for i in range(1, 14):
        t.forward(s)
        t.right(27.6923)
    wn.exitonclick()
def main():
    t = turtle.Turtle()
    length = 10 * (int(input("Please choose the length of the sides: ")))
    x = int(input("What x coordinate would you like the tridecagon to start at?: "))
    y = int(input("What y coordinate would you like the tridecagon to start at?: "))
    tridecagonTurtle(length, x, y, t)
if __name__ == "__main__":
    main()