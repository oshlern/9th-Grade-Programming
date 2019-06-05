import random
def main(turnNumber, opponentsMoves, yourMoves):
    if turnNumber <= 1:
        return random.choice([False,True])
    avg = sum(opponentsMoves)/(turnNumber-1)
    return avg>0.5
