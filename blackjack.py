deck=[]
cards=[]
Dcards=[]
def setDeck():
    deck=[]
    for j in ("hearts","diamonds","clubs","spades"):
        for i in range(1,13):
            deck+=[i,j]
def shuffleDeck:

def DcardGenerate(mode):
    if mode=="initial":
        Dcards+=[deck.pop(0)]
        Dcards+=[deck.pop(0)]
    elif mode=="final":
        while cardSum(d)<17:
            Dcards+=[deck.pop(0)]
    if cardSum(d)>21:
        winRound()
def cardSum(player):
    sum=0
    if player=="p":
        for i in cards:
            sum+=i[0]
    elif player=="d":
        for i in Dcards:
            sum+=i[0]
    return sum
def loseRound():

def winRound():

def hit():
    cards+=[deck.pop(0)]
    if cardSum(p)>21:
        loseRound()
def stay():
    DcardGenerate("final")
    if cardSum(p)>cardSum(d):
        winRound()
    else
        loseRound()
