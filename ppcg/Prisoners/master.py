from __future__ import division
import random
# add a second probability? add randomness?
def main(turnNumber, opMoves, myMoves):
    totalTurnNum = 20
    sSignature = [0,0,1,0,1]
    mSignature = [1,0,0,1,0]
    def strat():
        return opMoves[-1]

    if turnNumber <= len(mSignature):
        return mSignature[turnNumber-1]
    if turnNumber <= len(sSignature):
        if opMoves[:len(sSignature)] == sSignature:
            if turnNumber > len(sSignature) + 1:
                if 0 in opMoves[len(sSignature):]:
                    return strat()
            return False
    return strat


print main(4,[0,1,0],[1,1,1])
