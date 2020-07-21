import copy
# map = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
# map = [[0, 0, 0, 0, 0, 0],
# [1, 1, 1, 1, 1, 0],
# [0, 0, 0, 0, 0, 0],
# [0, 1, 1, 1, 1, 1],
# [0, 1, 1, 1, 1, 1],
# [0, 0, 0, 0, 0, 0]]
map = [
[0, 0, 0, 0, 0, 0, 1, 0, 0],
[1, 1, 1, 1, 1, 0, 0, 1, 0],
[0, 0, 1, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 1, 0, 0, 0],
[0, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0]]

lowest, highDiff, maze, w, h, minVal, minAchieved = [1000, []], -2, [], 0, 0, 0, False
# ONLY FINDS SHORTCUTS, not new paths
# Reduce function calls
# Branch out from end, f
def adjacent(coords):
    out = []
    if coords[0] != w-1:
        out.append([coords[0]+1, coords[1]])
    if coords[1] != h-1:
        out.append([coords[0], coords[1]+1])
    if coords[0] != 0:
        out.append([coords[0]-1, coords[1]])
    if coords[1] != 0:
        out.append([coords[0], coords[1]-1])
    return out
    # order matters

def labelRecursivePath(current, coords, path):
    global minAchieved
    path.append(coords)
    maze[coords[0]][coords[1]] = current
    adjs = adjacent(coords)
    for adj in adjs:
        adjSpot = maze[adj[0]][adj[1]]
        if adjSpot == 0 or (adjSpot != -1 and adjSpot > current):
            nextVal = current + 1
            if adj == [w-1, h-1]:
                global lowest
                if nextVal < lowest[0]:
                    if nextVal == minVal:
                        minAchieved = True
                    lowest = [nextVal, [path]]
                elif nextVal == lowest[0]:
                    lowest[1].append(path)
                return
            labelRecursivePath(nextVal, adj, path)
            if minAchieved:
                return

def labelmap(map):
    global maze
    maze = [[-element for element in row] for row in map]
    coords = [0, 0]
    current = 1
    labelRecursivePath(current, coords, [])
    for row in maze:
        print row

# track path and then edit path based on just how much you subtracted from item in path

def checkWallFiltered(wall, adjs):
    lowAdj = 1000
    for adj in adjs:
        adj = maze[adj[0]][adj[1]]
        if adj < lowAdj and adj != 0:
            lowAdj = adj
    labelRecursive(lowest + 1, wall)
    return maze[w-1][h-1]

def checkWallPath(wall, adjs):
    lowAdj = 1000
    for adj in adjs:
        adj = maze[adj[0]][adj[1]]
        if adj < lowAdj and adj != 0:
            lowAdj = adj
    for adj in adjs:
        for path in lowest[1]:
            if adj in path: #TODO: Works? (multiple paths)
                diff = maze[adj[0]][adj[1]] - lowAdj
                global highDiff
                if diff > highDiff:
                    # print wall
                    # print diff
                    highDiff = diff
    return maze[w-1][h-1]

def findWallsFiltered(map):
    walls = []
    for i in range(w):
        for j in range(h):
            if map[i][j] == 1:
                adjOpen = [adj for adj in adjacent([i,j]) if map[adj[0]][adj[1]] == 0]
                if len(adjOpen) > 1:
                    walls.append([[i,j], adjOpen])
    return walls

def answerPath(map):
    global w, h, maze, lowest, highDiff
    w, h = len(map), len(map[0])
    minVal = w + h - 1
    labelmap(map)
    if minAchieved:
        return minVal
    newmap = copy.deepcopy(maze)
    print lowest, "Lowest"
    for wall in findWallsFiltered(map): #[[[i,j] for j in range(h) if map[i][j] == 1] for i in range(w)]
        # print wall
        checkWallFiltered(wall[0], wall[1])
        if minAchieved:
            return minVal
        maze = copy.deepcopy(newmap)
    return lowest[0] - highDiff + 2

def answer(map):
    global w, h, maze, lowest, highDiff
    w, h = len(map), len(map[0])
    minVal = w + h - 1
    labelmap(map)
    newmap = copy.deepcopy(maze)
    low = maze[w-1][h-1]
    if low == minVal:
        return minVal
    for wall in findWalls(map):
        attempt = checkWall(wall)
        if attempt < low:
            if low == minVal:
                return minVal
            low = attempt
        maze = copy.deepcopy(newmap)
    return low




# Branch out from beginning and end separately
# Mark each tile by how many steps it takes to get there (0 for impossible, -1 for wall)(for each?)
# When removing a wall, all the adjacerntnumbers (that are above 2 over the lowest numbers or 0) become lowest number +2
# Their adjacents may decrease as well
# maze, w, h = [], 0, 0
#
# def adjacent(coords):
#     out = []
#     if coords[0] != 0:
#         out.append([coords[0]-1, coords[1]])
#     if coords[0] != w-1:
#         out.append([coords[0]+1, coords[1]])
#     if coords[1] != 0:
#         out.append([coords[0], coords[1]-1])
#     if coords[1] != w-1:
#         out.append([coords[0], coords[1]+1])
#     return out
#
#
# def labelRecursive(current, coords):
#     global maze
#     maze[coords[0]][coords[1]] = current
#     adjs = adjacent(coords)
#     for adj in adjs:
#         adjSpot = maze[adj[0]][adj[1]]
#         if adjSpot == 0 or (adjSpot != -1 and adjSpot > current):
#             nextVal = current + 1
#             labelRecursive(nextVal, adj)
#
# def labelmap(map):
#     global maze
#     maze = [[-element for element in row] for row in map]
#     coords = [0, 0]
#     current = 1
#     labelRecursive(current, coords)
#
# def checkWall(wall):
#     adjs = [maze[adj[0]][adj[1]] for adj in adjacent(wall)]
#     lowest = 1000000
#     for adj in adjs:
#         if adj < lowest and adj > 0:
#             lowest = adj
#     labelRecursive(lowest + 1, wall)
#     return maze[w-1][h-1]
#
#
# def findWalls(map):
#     walls = []
#     for i in range(w):
#         for j in range(h):
#             if map[i][j] == 1:
#                 walls.append([i,j])
#     return walls
#
# def answer(map):
#     global w, h, maze
#     w, h = len(map), len(map[0])
#     labelmap(map)
#     # newmap = copy.deepcopy(maze)
#     lowest = maze[w-1][h-1]
#     for wall in findWalls(map):
#         attempt = checkWall(wall)
#         print "WALL: ", wall, attempt
#         print "___maze AFTER___"
#         for row in maze:
#             print row
#         if attempt < lowest:
#             lowest = attempt
#         # maze = copy.deepcopy(newmap) #make sure this works with variable reference and globality
#         labelmap(map)
#     return lowest


print answer(map)

    # adjacent +1 (iterate helper function?)
    # return
#
# def affectmaze(maze): #, walls):
#     return
#
# for i in walls:
#     lowest of affectmaze()[-1][-1]
#
# [0, 0, 0, 0, 0, 0],
# [1, 1, 1, 1, 1, 0],
# [0, 0, 0, 0, 0, 0],
# [0, 1, 1, 1, 1, 1],
# [0, 1, 1, 1, 1, 1],
# [0, 0, 0, 0, 0, 0]]
# def digits(num, b):
#     digits = []
#     while num >= 1:
#         digits.append(num % 10)
#         num /= 10
#     return digits
#
# def iterate(ds, b, k):
#     sortDs = sorted(ds)
#     subtracted = [sortDs[-i-1] - sortDs[i] for i in range(k)]
#     for i in range(k-1,0,-1):
#         if subtracted[i] < 0:
#             subtracted[i-1] -= 1
#             subtracted[i] = subtracted[i] % b
#         else:
#             break
#     subtracted[0] = subtracted[0] % b
#     return subtracted
#
# def analyzePath(path):
#     length = len(path) - 1
#     num = path[length]
#     return length - path.index(num)
#
# def answer(n, b):
#     num = digits(int(n), int(b))
#     k = len(num)
#     path = []
#     while not num in path:
#         path.append(num)
#         num = iterate(num, b, k)
#     path.append(num)
#     return analyzePath(path)
#     # your code here
#
# print answer(210022,3)
