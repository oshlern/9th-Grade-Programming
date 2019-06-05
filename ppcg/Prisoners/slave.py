from __future__ import division
import random
# add a second probability? add randomness?
def main(turnNumber, opMoves, myMoves):
    totalTurnNum = 20
    sSignature = [0,0,1,0,1]
    mSignature = [1,0,0,1,0]
    sig = 0
    if len(mSignature) < len(sSignature):
        sig = len(sSignature)
    else:
        sig = len(mSignature)
    if turnNumber <= len(sSignature):
        return sSignature[turnNumber-1]
    if turnNumber <= len(mSignature):
        if opMoves[:len(mSignature)] == mSignature:
            if turnNumber > sig + 1:
                if 1 in opMoves[sig:]:
                    return False
            return True
    return False


print main(4,[0,1,0],[1,1,1])
