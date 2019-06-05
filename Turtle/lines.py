import turtle
import random

turtle.screensize(1500, 1500)
turtle.setworldcoordinates(-10000, -10000, 10000, 10000)
turtle.speed("fastest")
turtle.color("blue")


x=1

for index in range(100000):
    turtle.forward(20)
    turtle.left(x*turtle.ycor()-turtle.xcor())
    x=x+0.1
