import turtle
import random

turtle.screensize(1500, 1500)
turtle.setworldcoordinates(-1000, -1000, 1000, 1000)
turtle.speed("fastest")
turtle.colormode(255)
string = "010203040506070809101112131415161718192021222324252627282930"


for x in range(1000):
    a=x+1
    x=turtle.Turtle()
    x.speed("fastest")
    x.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    x.right(random.randint(1,360))
    x.forward(2*a)
    x.circle(a,a)
    x.right(a)
    x.forward(50*random.random())
