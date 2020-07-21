teams = ['X', 'O']

print [1,2,3,1,1].index(1)
def replace(curState):
    if type(curState) == str:
        if curState == myTeam: return 1
        if curState == opTeam: return -1
        return 0
    return [replace(section) for section in curState]

# def canWinRow(row):
#     return sum(row)/2
#
# def canWin(curState):
#     out = []
#     for i in range(3):
#         out += [canWinRow(curState[i]), [i, 0.index(curState[i])]
#         out += [canWinRow(curState[:][i]), [0.index(curState[:][i]), i]
#     out += [canWinRow([curState[i][i] for i in range(3)]), [0.index(curState[curState[i][i] for i in range(3)])]*2]
#     out += [canWinRow([curState[2-i][i] for i in range(3)]), [0.index(curState[curState[2-i][i] for i in range(3)])]*2]
#     return [[row for row in out if row[0] == 1], [row for row in out if row[0] == -1]]
#
#

# def evaluateAndSpace(curState):
#     rows = {-2:[], -1:[], 0:[], 1:[], 2:[]} #can turn into array
#     for i in range(3):
#         rows[sum(curState[i])].append([i, curState[i].index(0)])
#         rows[sum(curState[:][i])].append(curState[:][i].index(0), i])
#     rows[sum([curState[i][i] for i in range(3)])].append([curState[i][i] for i in range(3)].index(0)))
#     rows[sum([curState[2-i][i] for i in range(3)])].append([[curState[2-i][i] for i in range(3)].index(0)])#fix
#     return rows

def evaluate(curState):
    rows = {-2: 0, -1: 0, 0: 0, 1: 0, 2: 0} #can turn into array
    for i in range(3):
        rows[sum(curState[i])] += 1
        rows[sum(curState[:][i])] += 1
    rows[sum([curState[i][i] for i in range(3)])] += 1
    rows[sum([curState[2-i][i] for i in range(3)])] += 1
    return rows
    # Row with 1 and -1 is an actual 0, empty row is ~0.3

def evaluateBoard(teamNum, curstate):
    state = evaluate(curState)
    if len(state[teamNum * 2]) != 0:
        return 1
    return len(state[teamNum]) // 10
    # Add evaluation based on other board states   evaluation*numOfMovesMade (by one player) in in its row and column (and diag) tsits coordinates are part of a row

#def evaluateBoards(curstate, wonBoards):
    #out = evaluateBoard(wonBoards)
    #individual board check

# def evaluateLayers(curState, activeBoardNum, wonBoards, teamNum, n):
#     if won(wonBoards) != 0:
#         return won(wonBoards)
#
#     value = 0 #[]
#     if not activeBoardNum in wonBoards:
#         value = evaluateBoard(-teamNum, curState[activeBoardNum[0]][activeBoardNum[1]])
#
#     evaluateLayers(curState, curState, activeBoardNum, wonBoards, -teamNum, n-1)

def possibleMoves(board):
    out = []
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == 0:
                out.append([i,j])
    return out

def won(curState):
    for i in range(3):
        row = sum(curState[i])
        column = sum(curState[:][i])
        if row == 3 or column == 3:
            return 1
        if row == -3 or column == -3:
            return -1
    diag1 = sum([curState[i][i] for i in range(3)])
    diag2 = sum([curState[2-i][i] for i in range(3)])
    if diag1 == 3 or diag2 == 3:
        return 1
    if diag1 == -3 or diag2 == -3:
        return -1
    return 0

def recurse(curState, activeBoardNum, wonBoards, myTeam, n):
    if won(wonBoards) != 0:
        return won(wonBoards)
    if n == 0:
        return evaluateBoard(wonBoards)
    activeBoard = curState[activeBoardNum[0]][activeBoardNum[1]]
    possibleMoves = [[i, j] for j in range(3) for i in range(3) if activeBoard[i][j] == 0]
    if len(possibleMoves == 0):
        return won(wonBoards)
    out = []
    for move in possibleMoves:
        boards = wonBoards
        curState[activeBoardNum[0]][activeBoardNum[1]][move[0]][move[1]] = myTeam
        if wonBoards[activeBoardNum[0]][activeBoardNum[1]] == 0 and won(activeBoard) != 0:
            boards[activeBoardNum[0]][activeBoardNum[1]] = won(activeBoard)
        out.append(recurse(curState, move, boards, -myTeam, n-1))
        curState[activeBoardNum[0]][activeBoardNum[1]][move[0]][move[1]] = 0

def winRecurse(state):
    if type(state) == list:
        for move in state:
            canWin = 0
            if type(move) == list:
                if 1 in [winRecurse(nextMove) for nextMove in move]:
                    canWin = 1
            else:
                canWin = move
            if canWin != 1:
                return 0
    return state

def canWin(curState, activeBoardNum, wonBoards, myTeam, n):
    if won(wonBoards) != 0:
        return won(wonBoards)
    if n == 0:
        return evaluateBoard(wonBoards)
    activeBoard = curState[activeBoardNum[0]][activeBoardNum[1]]
    possibleMoves = [[i, j] for j in range(3) for i in range(3) if activeBoard[i][j] == 0]
    if len(possibleMoves == 0):
        return won(wonBoards)
    out = []
    for move in possibleMoves:
        boards = wonBoards
        curState[activeBoardNum[0]][activeBoardNum[1]][move[0]][move[1]] = myTeam
        if wonBoards[activeBoardNum[0]][activeBoardNum[1]] == 0 and won(activeBoard) != 0:
            boards[activeBoardNum[0]][activeBoardNum[1]] = won(activeBoard)
        nextMoves = [[i, j] for j in range(3) for i in range(3) if curState[move[0]][move[1]][i][j] == 0]
        if len(nextMoves == 0):
            return won(wonBoards)
        nextOut = []
        for nextMove in nextMoves:
            nextBoards = boards
            curState[move[0]][move[1]][move[0]][move[1]] = myTeam
            if wonBoards[move[0]][move[1]] == 0 and won(curState[move[0][1]) != 0:
                boards[move[0]][move[1]] = won(curState[move[0][1])
            nextOut.append(winRecurse(recurse(curState, nextMove, nextBoards, myTeam, n-2)))
            curState[move[0]][move[1]][nextMove[0]][nextMove[1]] = 0
        canWin = 0
        if 1 in nextOut:
            canWin = 1
        out.append(canWin)
        curState[activeBoardNum[0]][activeBoardNum[1]][move[0]][move[1]] = 0
    return out.index(1)


def sumRecurse(state):
    if type(state) == list:
        return sum([sumRecurse(ministate) for ministate in state])
    return state


# def evaluateRecurse(curState, activeBoardNum, wonBoards, n):
#     state = recurse(curState, activeBoardNum, wonBoards, teamNum, n)
#     #state = [sumRecurse(ministate) for ministate in state]
#     #sort(state), get out move location
#     for ministate in state:
#         if
#     # bottom to top. if for all moves there is a winning move, do that

# def ticTac(curState):
#     state = evaluate(curState)
#
#     if len(rows[2] > 0):
#         return rows[2][0]


# def defensive():
#     print "hi"
#     #place in row with most enemy stuff
# def offensive():
#     print "hi"
#     #place in row with most my team stuff
def main(teamNum, curState, activeBoardNum, wonBoards):
    myTeam = teams[teamNum]
    opTeam = teams[teamNum-1]
    curState, wonBoards = replace(curState), replace(wonBoards)
    return canWin(curState, activeBoardNum, wonBoards, teamNum, n)
    # evaluate board of each possible move (of each possible move?)
    # evaluate the whole board using evaluateState?

    # for move in possibleMoves
    evaluatedMoves = {}
    # for move in possibleMoves:
        # evaluatedMoves.append(-teamNumevaluateBoard[curState[move]])
