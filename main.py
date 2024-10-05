# Turtle and Random module
import turtle
import random
from turtle import *

# List of colors
color = [(233, 233, 232), (231, 233, 237), (235, 231, 233), (224, 233, 227), (207, 159, 82), (54, 89, 130), (146, 91, 39), (140, 26, 48), (222, 207, 104), (132, 177, 203), (158, 46, 83), (45, 55, 104), (170, 160, 39), (129, 189, 143), (83, 20, 44), (36, 43, 69), (186, 94, 106), (186, 140, 172), (84, 120, 180), (60, 39, 31), (88, 157, 92), (78, 153, 164), (195, 78, 72), (45, 74, 78), (80, 74, 44), (162, 201, 218), (58, 126, 122), (218, 176, 187), (169, 207, 170), (220, 181, 168)]

# Changing the rgb color mode to 255
turtle.colormode(255)

# turtle Object
tim = Turtle()
# taking the pen from the canva and moving the turtle to the left bottom of the screen with seth and forward functions
tim.penup()
tim.setheading(225)
tim.forward(500)
tim.setheading(0)

# setting the number of dots and changing the turtle speed to fastest
number_of_dots = 225
tim.speed("fastest")


# Using for loop to generate dots and setting the dot size and color
for dot in range(1, number_of_dots+1):
    tim.dot(20, random.choice(color))
    tim.forward(50)

    # Using if condition to check whether we have to move to a line or not (15 dot per line)
    if dot % 15 == 0:
        tim.left(90)
        tim.forward(50)
        tim.left(90)
        tim.forward(750)
        tim.setheading(0)

# Screen object
sc = Screen()
sc.mainloop()