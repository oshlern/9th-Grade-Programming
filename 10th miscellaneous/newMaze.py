sample1 = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
sample2 = [[0, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 0],
[0, 0, 0, 0, 0, 0],
[0, 1, 1, 1, 1, 1],
[0, 1, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 0]]
sample3 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
sample4 = [
[0, 0, 0, 0, 0, 0, 1, 0, 0],
[1, 1, 1, 1, 1, 0, 0, 1, 0],
[0, 0, 1, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 1, 0, 0, 0],
[0, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0]]
sample5 = [[0,1], [0,1]]
sample6 = [[0,0,1,1,0,0]]
sample7 = [
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 0, 0, 1, 0],
[1, 1, 1, 1, 1, 1, 1, 1, 0],
[0, 0, 0, 1, 0, 0, 1, 0, 0],
[0, 1, 0, 0, 0, 1, 1, 1, 1],
[0, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0]]
# If a cell is passed, it should never be returned to unless it was passed by passing a wall and the current path hasn't passed a wall
# 5 or 6

w, h, width, height, maze = 0, 0, 0, 0, []
# visual = []
finished = False
solution = 0

def adjacent(coords):
    out = []
    if coords[0] != w:
        out.append([coords[0]+1, coords[1]])
    if coords[1] != h:
        out.append([coords[0], coords[1]+1])
    if coords[0] != 0:
        out.append([coords[0]-1, coords[1]])
    if coords[1] != 0:
        out.append([coords[0], coords[1]-1])
    print "out", out
    return out
    # order matters

def near(current, coords, wallNotPassed):
    global finished, solution
    print current, coords
    if wallNotPassed:
        maze[coords[0]][coords[1]] = -1 #doesn't work, wait actually it does. Wait no it doesn't
    else:
        maze[coords[0]][coords[1]] = -2
    adjs = adjacent(coords)
    out = []
    current = current + 1
    if coords == [w, h]:
        finished = True
        solution = current
        return
    for adj in adjs:
        adjSpot = maze[adj[0]][adj[1]]
        if adjSpot == 1:
            if wallNotPassed:
                out.append([current, adj, False])
        elif adjSpot == 0:

            out.append([current, adj, wallNotPassed])
        elif adjSpot == -2 and wallNotPassed:
            out.append([current, adj, wallNotPassed])
    return out

def NewLabelmaze():
    global maze #, visual
    for row in range(width):
        for column in range(height):
            if maze[row][column] == 1:
                if len([adj for adj in adjacent([row, column]) if maze[adj[0]][adj[1]] == 0]) < 2:
                    maze[row][column] = -1
                ## save adjacents for later? label adjacent of everything?
    # visual = list(maze)
    moves = near(1, [0, 0], True)
    while moves != []:
        nextMove = moves.pop()
        newMoves = near(nextMove[0], nextMove[1], nextMove[2])
        if finished:
            return
        print moves
        moves += newMoves

def labelRecursive(current, coords, wallNotPassed):
    # print maze
    global finished, solution
    # visual[coords[0]][coords[1]] = current
    # print "___VISUAL____"
    # for row in visual:
    #     print row
    if wallNotPassed:
        maze[coords[0]][coords[1]] = -1 #doesn't work, wait actually it does. Wait no it doesn't
    else:
        maze[coords[0]][coords[1]] = -2
    current, out, adjs = current + 1, [], []
    if coords[0] != w:
        adjs.append([coords[0]+1, coords[1]])
    elif coords[1] == h-1:
        finished = True
        solution = current
        return
    if coords[1] != h:
        adjs.append([coords[0], coords[1]+1])
    elif coords[0] == w-1:
        finished = True
        solution = current
        return
    if coords[1] != 0:
        spot = maze[coords[0]][coords[1]-1]
        if spot == 1:
            if wallNotPassed:
                out.append([current, [coords[0], coords[1]-1], False])
        elif spot == 0:
                out.append([current, [coords[0], coords[1]-1], wallNotPassed])
    if coords[0] != 0:
        spot = maze[coords[0]-1][coords[1]]
        if spot == 1:
            if wallNotPassed:
                out.append([current, [coords[0]-1, coords[1]], False])
        elif spot == 0:
                out.append([current, [coords[0]-1, coords[1]], wallNotPassed])
        # out.append([current, [coords[0]-1, coords[1]], wallNotPassed])
    for adj in adjs:
        adjSpot = maze[adj[0]][adj[1]]
        if adjSpot == 1:
            if wallNotPassed:
                nextOut = labelRecursive(current, adj, False)
                if finished:
                    return
                for move in nextOut:
                    out.append(move)
        elif adjSpot == 0:
            nextOut = labelRecursive(current, adj, wallNotPassed)
            if finished:
                return
            for move in nextOut:
                out.append(move)
        elif adjSpot == -2 and wallNotPassed:
            nextOut = labelRecursive(current, adj, wallNotPassed)
            if finished:
                return
            for move in nextOut:
                out.append(move)
    return out

def labelmaze():
    global maze #, visual
    for row in range(width):
        for column in range(height):
            if maze[row][column] == 1:
                if len([adj for adj in adjacent([row, column]) if maze[adj[0]][adj[1]] == 0]) < 2:
                    maze[row][column] = -1
                ## save adjacents for later? label adjacent of everything?
    # visual = list(maze)
    moves = labelRecursive(1, [0, 0], True)
    if finished:
        return
    while moves != []:
        nextMove = moves.pop()
        newMoves = labelRecursive(nextMove[0], nextMove[1], nextMove[2])
        if finished:
            return
        moves += newMoves


def answer(problem):
    global w, h, maze, width, height #necessary?
    maze = problem
    width, height = len(problem), len(problem[0])
    w, h = width - 1, height - 1
    labelmaze()
    return solution

print answer(sample7)
