
#basic turtle game using turtle graphicsimport time

import turtle
import time
from turtle import Turtle
from random import randint
from turtle import *
import subprocess
import os
import sys, random




# window for the game
window = turtle.Screen() # Screen object created
window.setup(width = 1.0, height = 1.0)
window.title("GO TURTLE GO") # title that apperars on top of the wondow
turtle.hideturtle()

turtle.color("maroon")# title color
turtle.penup()
turtle.bgpic("water.gif")
turtle.update()
turtle.speed(0)    # not running
turtle.penup()
turtle.setpos(-140,200) 
turtle.write("GO TURTLES GO", font=("Times New Roman", 40, "bold"),align="center" )


# music file 
subprocess.call(["afplay", "music/Applause.wav"])
    
# turtle 1
# positioning turtles 

turtle1 = Turtle()
turtle1.speed(0)
turtle.penup()
turtle1.color("black")
turtle1.shape("turtle")
turtle1.penup()
turtle1.goto(-250,100)

# turtle 2
turtle.penup()
turtle2 = Turtle()
turtle2.speed(0)
turtle2.color("red")
turtle2.shape("turtle")
turtle2.penup()
turtle2.goto(-250,50)


# turtle 3
turtle3 = Turtle()
turtle3.speed(0)
turtle3.color("Green")
turtle3.shape("turtle")
turtle3.penup()
turtle3.goto(-250,0)


# turtle 4

turtle4 = Turtle()
turtle4.speed(0)
turtle4.color("white")
turtle4.shape("turtle")
turtle4.penup()
turtle4.goto(-250,-50)


# turtle 5

turtle5 = Turtle()
turtle5.speed(0)
turtle5.color("grey")
turtle5.shape("turtle")
turtle5.penup()
turtle5.goto(-250,-100)

    
# turtle 6

turtle6 = Turtle()
turtle6.speed(0)
turtle6.color("yellow")
turtle6.shape("turtle")
turtle6.penup()
turtle6.goto(-250,-150)

time.sleep(1) # pauses the game for 1 sec before starting the game
# music file 2
subprocess.call(["afplay", "music/GetReady.wav"])

# game end line using square 
stampSize = 20
square_size = 15
finishLine = 430

turtle.color("black")

turtle.shape("square")
turtle.shapesize( square_size / stampSize)
turtle.penup()
for i in range(13):
    turtle.setpos(finishLine, (150 - ( i * square_size * 2)))
    turtle.stamp()


# turtles speed

for i in range(227): # forward turtle 
    
    turtle.penup()
    turtle1.forward(randint(1,5))
    turtle2.forward(randint(1,5))
    turtle3.forward(randint(1,5))
    turtle4.forward(randint(1,5))
    turtle5.forward(randint(1,5))
    turtle6.forward(randint(1,5))
    
subprocess.call(["afplay", "music/Applause.wav"])
turtle.exitonclick()

 
