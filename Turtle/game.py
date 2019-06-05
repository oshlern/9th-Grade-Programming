import turtle
p1=turtle.Turtle()
p1.shape("turtle")
p1.color("blue")
p1.speed(0)
p1.pensize(3)
p1.pu()
p1.setpos(-200,100)
p1.pd()
a1=0

p2=turtle.Turtle()
p2.shape("turtle")
p2.color("red")
p2.speed(0)
p2.pensize(3)
p2.pu()
p2.setpos(-200,-100)
p2.pd()
a2=0

finishline=turtle.Turtle()
finishline.ht()
finishline.color("yellow")
finishline.pensize(5)
finishline.pu()
finishline.setpos(200,-330)
finishline.pd()
finishline.seth(90)
finishline.forward(700)


def press1(b):
    global a1
    if a1==b:
        forward1()
        if a1==0:
            a1=1
        else:
            a1=0

def press2(b):
    global a2
    if a2==b:
        forward2()
        if a2==0:
            a2=1
        else:
            a2=0

def forward1():
    p1.forward(5)

def forward2():
    p2.forward(5)

def circler1():
    p1.circle(10, 30)

def circlel1():
    p1.circle(-10, 30)

def circler2():
    p2.circle(10, 30)

def circlel2():
    p2.circle(-10, 30)

def p1wins():
    p1Win=turtle.Turtle()
    p1Win.ht()
    p1Win.speed(0)
    p1Win.color("blue")
    p1Win.pu()
    p1Win.setpos(-300, 50)
    p1Win.write("Player 1", font=("Helvetica", 150, "bold"))
    p1Win.setpos(-180, -200)
    p1Win.write("Wins!", font=("Helvetica", 150, "bold"))
    p1Win.pd()
    for uselessvar in range(40):
        p1Win.setpos(300-random.random()*600, 300-random.random()*600)
        p1Win.pensize(5)
        p1Win.circle(100*random.random(), 360)
        p1Win.pensize(2)

def p2wins():
    p2Win=turtle.Turtle()
    p2Win.ht()
    p2Win.color("red")
    p2Win.speed(0)
    p2Win.pu()
    p2Win.setpos(-300, 50)
    p2Win.write("Player 2", font=("Helvetica", 150, "bold"))
    p2Win.setpos(-180, -200)
    p2Win.write("Wins!", font=("Helvetica", 150, "bold"))
    p2Win.pd()
    for uselessvar in range(30):
        p2Win.setpos(300-random.random()*600, 300-random.random()*600)
        p2Win.pensize(5)
        p2Win.circle(100*random.random(), 360)
        p2Win.pensize(2)

turtle.onkey(press1(0), 'a')
turtle.onkey(press1(1), 'd')
turtle.onkey(circler1(), 'w')
turtle.onkey(circlel1(), 's')
turtle.onkey(press2(0), 'j')
turtle.onkey(press2(1), 'l')
turtle.onkey(circler2(), 'i')
turtle.onkey(circlel2(), 'k')
turtle.listen()

for var in range(10000000):
    if p1.xcor()>=198:
        p1wins()
    if p2.xcor()>=198:
        p2wins()
