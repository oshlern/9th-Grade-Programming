import turtle, random, time, math
#from TKinter import mainloop

turtle.colormode(255)
turtle.color("yellow")
turtle.delay(0.001)
turtle.speed(0)
turtle.pensize(2)
p1Point=0
p2Point=0
turtledelay=0.03
spd=8
dif=7

def easydif():
    global dif
    dif=10

def normdif():
    global dif
    dif=7

def harddif():
    global dif
    dif=4

def spdslow():
    global spd
    spd=1
    p1.speed(spd)
    p2.speed(spd)

def spdnormal():
    global spd
    spd=5
    p1.speed(spd)
    p2.speed(spd)

def spdfast():
    global spd
    spd=0
    p1.speed(spd)
    p2.speed(spd)

def speed(str):
    global spd
    var = {"slow": 1, "normal": 5, "fast": 0}
    spd=var[str]
    p1.speed(spd)
    p2.speed(spd)

def turtlespeedeasy():
    global turtledelay
    turtledelay=0.08

def turtlespeednormal():
    global turtledelay
    turtledelay=0.03

def turtlespeedhard():
    global turtledelay
    turtledelay=0

def p1writer():
    global p1write
    p1write=turtle.Turtle()
    p1write.ht()
    p1write.pu()
    p1write.color("blue")
    p1write.setpos(-300, 250)
    p1write.write("Player 1  -  I J K L", font=("Helvetica", 25, "bold"))
    p1write.setpos(-255, 235)
    p1write.color("black")
    for uselessvar in range(10):
        p1write.write(".", font=("Helvetica", 50, "bold"))
        p1write.forward(10)
    p1write.setpos(-255, 235)
    p1write.color("red")

def p2writer():
    global p2write
    p2write=turtle.Turtle()
    p2write.ht()
    p2write.pu()
    p2write.color("red")
    p2write.setpos(90, 250)
    p2write.write("Player 2  -  W A S D", font=("Helvetica", 25, "bold"))
    p2write.setpos(135, 235)
    p2write.color("black")
    for uselessvar in range(10):
        p2write.write(".", font=("Helvetica", 50, "bold"))
        p2write.forward(10)
    p2write.setpos(135, 235)
    p2write.color("blue")

def setupP1():
    global p1
    p1 = turtle.Turtle()
    p1.shape("turtle")
    p1.speed(8)
    p1.color("blue")
    p1.pu()
    p1.setpos(100, 0)
    p1.pd()
    p1.pensize(2)
    p1.seth(90)

def setupP2():
    global p2
    p2 = turtle.Turtle()
    p2.shape("turtle")
    p2.speed(8)
    p2.color("red")
    p2.pu()
    p2.setpos(-100, 0)
    p2.pd()
    p2.pensize(2)
    p2.seth(90)

def p1PointUp():
    global p1Point
    p1Point=p1Point+1
    p1write.write(".", font=("Helvetica", 50, "bold"))
    p1write.forward(10)

def p2PointUp():
    global p2Point
    p2Point=p2Point+1
    p2write.write(".", font=("Helvetica", 50, "bold"))
    p2write.forward(10)

def forward():
    p1.seth(90)
    p1.forward(5)
#    p1.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))

def back():
    p1.seth(270)
    p1.forward(5)
#    p1.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))

def right():
    p1.seth(0)
    p1.forward(5)
#    p1.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))

def left():
    p1.seth(180)
    p1.forward(5)
#    p1.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))

def w():
    p2.forward(5)
#    p2.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))

def s():
    p2.forward(-5)
#    p2.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))

def a():
    p2.circle(30,30)
#    p2.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))

def d():
    p2.circle(-30,30)
#    p2.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))

def rand():
    global spd
    p1.speed(0)
    p2.speed(0)
    p1.seth(360*random.random())
    p1.forward(100)
    p2.seth(360*random.random())
    p2.forward(100)
    p1.speed(spd)
    p2.speed(spd)
#    p1.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
#    p2.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))

def p1Winner():
    global p1Point
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
        p1Win.pensize(2)
        p1Win.circle(100*random.random(), 360)
        p1Win.pensize(1)

    p1Point=0
#   add extra animation
#   Time.sleep(100)

def p2Winner():
    global p2Point
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
        p2Win.pensize(2)
        p2Win.circle(100*random.random(), 360)
        p2Win.pensize(1)
    p2Point=0
#   add extra animation
#   Time.sleep(100)

def game_over():
    GameOver=turtle.Turtle()
    GameOver.ht()
    GameOver.pu()
    GameOver.setpos(-250, 20)
    GameOver.write("Game", font=("Helvetica", 180, "bold"))
    GameOver.setpos(-200, -200)
    GameOver.write("Over", font=("Helvetica", 180, "bold"))
#   Time.sleep(100)

def Bounce():
    global spd
    x=random.random()*270-135
    p1.speed(0)
    p2.speed(0)
    p1.right(x)
    p2.right(x)
    p1.forward(150)
    p2.forward(150)
    p1.speed(spd)
    p2.speed(spd)
#change to bounce backwards

def LookForPointsAndBounces():
    global p1X
    global p1Y
    global p2X
    global p2Y
    global tX
    global tY
    global dif
    p1X=p1.xcor()
    p1Y=p1.ycor()
    p2X=p2.xcor()
    p2Y=p2.ycor()
    tX=turtle.xcor()
    tY=turtle.ycor()
    p1D=math.sqrt(math.pow((p1X-tX), 2)+math.pow((p1Y-tY), 2))
    p2D=math.sqrt(math.pow((p2X-tX), 2)+math.pow((p2Y-tY), 2))
    p1p2D=math.sqrt(math.pow((p1X-p2X), 2)+math.pow((p1Y-p2Y), 2))
    if p1D<=dif:
        p1PointUp()
        RandSnitch()
    if p2D<=dif:
        p2PointUp()
        RandSnitch()
    if p1p2D<=8:
        Bounce()

def tessellate():
    global spd
    if p1X>300:
        p1.speed(0)
        p1.pu()
        p1.setx(-300)
        p1.pd()
        p1.speed(spd)
    if p2X>300:
        p2.speed(0)
        p2.pu()
        p2.setx(-300)
        p2.pd()
        p2.speed(spd)
    if tX>300:
        turtle.pu()
        turtle.setx(-300)
        turtle.pd()

    if p1Y>300:
        p1.speed(0)
        p1.pu()
        p1.sety(-300)
        p1.pd()
        p1.speed(spd)
    if p2Y>300:
        p2.speed(0)
        p2.pu()
        p2.sety(-300)
        p2.pd()
        p1.speed(spd)
    if tY>300:
        turtle.pu()
        turtle.sety(-300)
        turtle.pd()

    if p1X<-300:
        p1.speed(0)
        p1.pu()
        p1.setx(300)
        p1.pd()
        p1.speed(spd)
    if p2X<-300:
        p2.speed(0)
        p2.pu()
        p2.setx(300)
        p2.pd()
        p2.speed(spd)
    if tX<-300:
        turtle.pu()
        turtle.setx(300)
        turtle.pd()

    if p1Y<-300:
        p1.speed(0)
        p1.pu()
        p1.sety(300)
        p1.pd()
        p1.speed(spd)
    if p2Y<-300:
        p2.speed(0)
        p2.pu()
        p2.sety(300)
        p2.pd()
        p2.speed(spd)
    if tY<-300:
        turtle.pu()
        turtle.sety(300)
        turtle.pd()

def RandSnitch():
    turtle.setpos(300-600*random.random(), 300-600*random.random())

def Restart():
    p1.reset()
    p2.reset()
    p1write.reset()
    p2write.reset()
    p1Win.reset()
    p2Win.reset()
    GameOver.reset()
    turtle.reset()
    game()

def KeyBindings():
    turtle.onkey(turtlespeedeasy, '1')
    turtle.onkey(turtlespeednormal, '2')
    turtle.onkey(turtlespeedhard, '3')
    turtle.onkey(speed("slow"), '4')
    turtle.onkey(speed("normal"), '5')
    turtle.onkey(speed("fast"), '6')
    turtle.onkey(easydif, '7')
    turtle.onkey(normdif, '8')
    turtle.onkey(harddif, '9')
    turtle.onkey(forward, 'i')
    turtle.onkey(back, 'k')
    turtle.onkey(right, 'l')
    turtle.onkey(left, 'j')
    turtle.onkey(w, 'w')
    turtle.onkey(s, 's')
    turtle.onkey(a, 'a')
    turtle.onkey(d, 'd')
    turtle.onkey(rand, 'r')
    turtle.onscreenclick(turtle.goto)
    turtle.listen()
#    turtle.onkey(Restart, '0')

def game():
    p1writer()
    p2writer()
    setupP1()
    setupP2()
    KeyBindings()
    turtle.ontimer(game_over, 120000)
    x=0
    for uselessvar in range(1000):
        global x
        if x==1:
            global turtle
            turtle.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
        else:
            turtle.color("yellow")
        turtle.right(90-180*random.random())
        for uselessvar in range(20):
            global turtledelay
            LookForPointsAndBounces()
            tessellate()
            turtle.forward(1)
            if p1Point>=10:
                p1Winner()
            if p2Point>=10:
                p2Winner()
            time.sleep(turtledelay)
        x=x-1
        x=math.pow(x, 2)

game()
