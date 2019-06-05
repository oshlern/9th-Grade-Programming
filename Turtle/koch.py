import turtle
turtle.pu()
turtle.setpos(-200,120)
turtle.pd()
turtle.speed(0)
# turtle.pensize(2)
# turtle.color("black")
def fractalLine(x,l,s):
    if x==l:
        turtle.forward(s/(3^x))
        turtle.left(60)
        turtle.forward(s/(3^x))
        turtle.right(120)
        turtle.forward(s/(3^x))
        turtle.left(60)
        turtle.forward(s/(3^x))
    else:
        turtle.color("white")
        fractalLine(x+1,l,s)
        turtle.left(60)
        turtle.color("blue")
        fractalLine(x+1,l,s)
        turtle.right(120)
        turtle.color("white")
        fractalLine(x+1,l,s)
        turtle.left(60)
        turtle.color("blue")
        fractalLine(x+1,l,s)
for i in range(3):
    fractalLine(0,1,10)
    turtle.right(120)

turtle.exitonclick()
