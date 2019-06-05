# cube = [
# ['top','forward'],['top','right'],['top','back'],['top','left'],
# ['mid','forwardr'],['mid','rightb'],['mid','backl'],['mid','leftf'],
# ['bottom','forward'],['bottom','right'],['bottom','back'],['bottom','left']]

# cube =[]
# for i in range(3):
#     layer=[]
#     for j in range(3):
#         row=[]
#         for k in range(3):
#             row+=[k+3*j+9*i]
#         layer+=[row]
#     cube+=[layer]
# print cube
cube = [[[13, 1, 14], [2,  0,  3], [15,  4, 16]],
        [[5,  0,  6], [0, -1,  0], [7,   0,  8]],
        [[17, 9, 18], [10, 0, 11], [19, 12, 20]]]
def top(cube):
    return cube[0]
def bot(cube):
    return cube[0]
def rig(cube):
    face = []
    for side in cube:
        face += [side[2]]
    return face
def lef(cube):
    face = []
    for side in range(3):
        face += [side[0]]
    return face
def fro(cube):
    face = []
    for side in cube:
        row = []
        for col in side:
            row += [col[0]]
        face += [row]
    return face
def bac(cube):
    face = []
    for side in cube:
        row = []
        for col in side:
            row += [col[2]]
        face += [row]
    return face
# rewrite without for loops, but hardcoded locations
def turn(face):
    return [[face[2][0], face[1][0], face[0][0]],
    [face[2][1], face[1][1], face[0][1]],
    [face[2][2], face[1][2], face[0][2]]]
def solveSP(i,j):
    turn(cube[])
