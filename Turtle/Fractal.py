import turtle
import random
import time


turtle.setworldcoordinates(-1000, -1000, 1000, 1000)

turtle.shape("turtle")
turtle.speed("fast")
turtle.colormode(255)
turtle.color(0,0,255)


r=0
b=255
p=1

#turtle.penup()
#turtle.right(210)
#turtle.forward(1600)
#turtle.right(150)
#turtle.pendown()
#turtle.forward(1)

for index in range(5):
    p=3^(index-1)
    for var1 in range(3):
        turtle.forward(243/p)
        if p>1:
            for var2 in range(p):
                turtle.right(300)
                turtle.forward(243/p)
                turtle.right(120)
                turtle.forward(243/p)
                turtle.right(300)
                turtle.forward(243/p)
        turtle.right(120)
        b=b-25
        r=r+25
        turtle.color(r,0,b)



time.sleep(5)
turtle.exitonclick
