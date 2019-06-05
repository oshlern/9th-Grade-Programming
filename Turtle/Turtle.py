import turtle
import random


turtle.screensize(1500, 1500)
turtle.setworldcoordinates(-500, -500, 500, 500)

turtle.speed("faster")
turtle.shape("turtle")
turtle.color("blue")

N=180
turtle.colormode(255)
for index in range(1000000):
    turtlex=turtle.xcor()
    turtley=turtle.ycor()
    turtle.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    N=N-random.random()
    turtle.right(N)
    turtle.forward(300*random.random())
    if turtlex > 300:
        turtle.setheading(180)
        turtle.forward(turtlex-300+150)
    if turtlex < -300:
        turtle.setheading(0)
        turtle.forward(-(turtlex)-300+150)
    if turtley > 300:
        turtle.setheading(180)
        turtle.forward(turtley-300+150)
    if turtley < -300:
        turtle.setheading(0)
        turtle.forward(-(turtley)-300+150)

turtle.exitonclick()
