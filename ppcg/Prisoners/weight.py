from __future__ import division
import random, math
def main(turnNumber, opponentsMoves, yourMoves):
    niceness = 9 #0-10
    outcomes = [[[1,1], [5,0]],[[0,5], [3,3]]]
    totalTurnNum = 20
    def costTurn(turnNumber, totalTurnNum, niceness):
        return 1-math.pow(turnNumber/totalTurnNum, math.pow(niceness, 0.85)/2) #5 is good. combine with * costTurn
    def weightAvg(moves, turnNumber):
        total = 0
        norm = 0
        for i in range(turnNumber-1):
            total += moves[i]/(turnNumber-i)
            norm += 1/(i+2)
        return total/norm
    if turnNumber == 1:
        return True
    return random.random() < weightAvg(opponentsMoves, turnNumber) * costTurn(turnNumber, totalTurnNum, niceness)
print main(4,[0,0,1,1],[1,1,1])
# remove randomness (don't ruin a working strategy)
# recursive nueral network
# find their patterns?
# value the latest moves more, add up to one. n-1: 1/2, n-2:1/3
#   find function(moveNum, turnNumber) that can distribute properly while adding up to one
# nash equilibrium = always rat. stems from last possible game
# lots of collaboration = good
# in the beginning trigger algorithms to cooperate and if they don't then confess
# tit for tat works miracles against itself (POINTS)
# convince others to add stuff to their programs which will get this program points, e.g. 'if they always cooperate, you should too'
# cost starts at 0 not 1
# only way to improve is to tie tit for tat and false and cooperate with others
# program is too complicated
# game is too stupid (tic tac toe tournament)
# make a tree to solve it
# delayed tit for tat?
# start with a strategy, change if it doesn't work, use best average strategy from the past moves based on return value
# true first and afterwards false
# non-forgiving strategy (after first?)
