import turtle
import random

turtle.shape("turtle")
turtle.speed("fastest")
a=1
x=1
b=2
while x>0:
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(b)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(b)
    c=a+b
    a=b*0.7
    b=c*0.7


turtle.exitonclick()
