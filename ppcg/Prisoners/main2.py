from __future__ import division
import random
# cooperate and betray when you can against others
def main(turnNumber, opponentsMoves, yourMoves):
    first = 1
    second = 0.6 #doesn't include oopponent true on first. ture is good for cooperation programs (avg or non-forgiving), false is good for mean/false programs, tit for tat is better with false or true depending on outcomes (currently true)
    totalTurnNum = 20
    def rand():
        tft = 0
        for i in range(turnNumber-1):
            if opponentsMoves[i+1] != yourMoves[i]:
                tft += 1
                # tft += (opponentsMoves[i+1]+yourMoves[i])%2
        tft /= turnNumber-1
        # avg programs?
        return 0
    # return (turnNumber<totalTurnNum) and  (turnNumber <= 1) or (turnNumber == 2) or
    if turnNumber >= totalTurnNum:
        return False
    if turnNumber <= 1:
        return random.random() < first
    if turnNumber == 2:
        if opponentsMoves[0]:
            return True
        return random.random() < second
    if turnNumber == 3:
        return opponentsMoves[1]
    if not 1 in opponentsMoves:
        return False
    if opponentsMoves[-1]==yourMoves[-2]:
        if random.random()<rand():
            return False
        return opponentsMoves[-1]
        # what if random? make sure to always say false (lots more points)
    return False
        # me: false, . | op: ., true
        # either they are gonna keep doing true, they have an inverted thing of what I'm doing, or they're forgiving
        # false is best in the first 2, and true can be better in the last, but program is unlikely and in an unlikely situation
# when to betray if against nice bot, how many nice bots vs. others
# can fail on: weird forgiving bot, random
# play with different values for second
# print main(2,[0],[1])
# one long function: first or (second or )
# predict future: if tftProb > 0.7
# obfuscate before submitting
