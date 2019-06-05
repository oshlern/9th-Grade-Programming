import turtle
import random
import time

turtle.screensize(1500, 1500)
turtle.setworldcoordinates(-10000, -10000, 10000, 10000)
turtle.speed("fastest")
turtle.colormode(255)


for a in range(100):
    for b in range(720):
        turtle.forward(a*b)
        turtle.right(a*b)
    turtle.seth(a)
