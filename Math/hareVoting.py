import operator
votes = [['A', 'B', 'C']]*5 + [['C', 'B', 'A']]*4 + [['B', 'C', 'A']]*3 + [['A', 'B', 'C']]
votes = [['A', 'B', 'C', 'D']]*100 + [['C', 'B', 'A', 'D']]*97 + [['D', 'B', 'C', 'A']]*56

def checkVotes(votes):
    candidates = {}
    for vote in votes:
        if not vote[0] in candidates:
            candidates[vote[0]] = 0
        candidates[vote[0]] += 1
    return candidates

def findLast(candidates):
    last, least = '', 10000
    for candidate in candidates:
        if candidates[candidate] < least:
            least = candidates[candidate]
            last = candidate
    return last

def delCand(candidate, votes):
    for i in range(len(votes)):
        if candidate in votes[i]:
            votes[i].remove(candidate)
    return votes

def runHare(votes):
    while len(votes[0])>1:
        votes = delCand(findLast(checkVotes(votes)), votes)
    return votes[0][0]

print runHare(votes)
