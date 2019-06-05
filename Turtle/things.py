import turtle, random
a=turtle.Turtle()
a.pensize(5)
a.speed(0)
a.seth(0)

b=turtle.Turtle()
b.color("white")
b.pensize(5)
b.speed(0)
b.seth(90)
x=0
y=0
z=0
w=0
turtle.colormode(255)
a.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))

def bmove(var1):
    if var1=="x":
        b.forward(10)
    elif var1=="y":
        b.forward(-10)
    elif var1=="z":
        b.circle(30,30)
    elif var1=="w":
        b.circle(-30,30)

def amove(var):
    if var=="x":
        a.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
        a.forward(10)
        turtle.ontimer(bmove('x'), 1500)
    elif var=="y":
        a.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
        a.forward(-10)
        turtle.ontimer(bmove('y'), 1500)
    elif var=="z":
        a.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
        a.circle(30,30)
        turtle.ontimer(bmove('z'), 1500)
    elif var=="w":
        a.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
        a.circle(-30,30)
        turtle.ontimer(bmove('w'), 1500)

turtle.onkey(amove('x'), 'w')
turtle.onkey(amove('y'), 's')
turtle.onkey(amove('z'), 'a')
turtle.onkey(amove('w'), 'd')
turtle.listen()
#make space

turtle.exitonclick()
