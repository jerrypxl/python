
import turtle
s = turtle.Screen()
turtle1 = turtle.Turtle('turtle')
turtle2 = turtle.Turtle('turtle')
import random


def setup(turtle1, turtle2, s):
    s.setworldcoordinates(0,0,50,50)
    turtle1.fillcolor('red')
    turtle1.pencolor('red')
    turtle2.fillcolor('red')
    turtle2.pencolor('red')
    turtle1.penup()
    turtle2.penup()
    turtle1.setposition(1,25)
    turtle2.setposition(1,25)
    turtle1.pendown()
    turtle2.pendown()

setup(turtle1, turtle2, s)


def newHeading(turtle, angleOfTipsiness):
    turtle.setheading(random.randint(-angleOfTipsiness, angleOfTipsiness))



def newColors(turtle1, turtle2):
    if turtle1.xcor() > turtle2.xcor():
        turtle1.fillcolor('green')
        turtle1.pencolor('green')
        turtle2.fillcolor('red')
        turtle2.pencolor('red')
    elif turtle1.xcor() < turtle2.xcor():
        turtle1.fillcolor('red')
        turtle1.pencolor('red')
        turtle2.fillcolor('green')
        turtle2.pencolor('green')



def tipsyTurtleRace(turtle1, turtle2, angleOfTipsiness, nSteps):
    for i in range(1,nSteps+1):
        newColors(turtle1, turtle2)
        newHeading(turtle1, angleOfTipsiness)
        newHeading(turtle2, angleOfTipsiness)
        turtle1.forward(1)
        turtle2.forward(1)

tipsyTurtleRace(turtle1, turtle2, 70, 50)


if turtle1.xcor() > turtle2.xcor():
    print('Leeroy won!')
elif turtle1.xcor() < turtle2.xcor():
    print('Jenkins won!')
else:
    print('It is a tie!')



