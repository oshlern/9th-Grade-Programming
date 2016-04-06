import random

reply=0
a=0

def rep(x):
    global reply
    if x==1:
        reply="Puter Plays:  rock"
    elif x==2:
        reply="Puter Plays:  paper"
    elif x==3:
        reply="Puter Plays:  scissors"
    elif x==4:
        reply="Puter Plays:  lizard"
    elif x==5:
        reply="Puter Plays:  spock"

def  puterwins():
    print("Puter Wins!")
def tie():
    print("It's a tie!")
def  youwin():
    print("You Win!")

def checkputerwins():
    if a==1 and (str(answer)=="paper" or str(answer)=="spock"):
        youwin()
    if a==2 and (str(answer)=="scissors" or str(answer)=="lizard"):
        youwin()
    if a==3 and (str(answer)=="rock" or str(answer)=="spock"):
        youwin()
    if a==4 and (str(answer)=="rock" or str(answer)=="scissors"):
        youwin()
    if a==5 and (str(answer)=="paper" or str(answer)=="lizard"):
        youwin()
def checktie():
    if a==1 and str(answer)=="rock":
        tie()
    if a==2 and str(answer)=="paper":
        tie()
    if a==3 and str(answer)=="scissors":
        tie()
    if a==4 and str(answer)=="lizard":
        tie()
    if a==5 and str(answer)=="spock":
        tie()
def checkyouwin():
    if (a==2 or a==5) and str(answer)=="rock":
        puterwins()
    if (a==3 or a==4) and str(answer)=="paper":
        puterwins()
    if (a==1 or a==5) and str(answer)=="scissors":
        puterwins()
    if (a==1 or a==3) and str(answer)=="lizard":
        puterwins()
    if (a==2 or a==4) and str(answer)=="spock":
        puterwins()

def whowins():
    checkputerwins()
    checktie()
    checkyouwin()

for uselessvar in range(10):
    a=random.randint(1,5)

    question = "You Play:     "
    answer = raw_input(question)
    rep(a)
    print(reply)

    whowins()
