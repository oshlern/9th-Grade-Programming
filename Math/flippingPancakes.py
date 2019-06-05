from __future__ import division

# Input

'''5
-
-+
+-
+++
--+-'''

'''Output
Case #1: 1
Case #2: 1
Case #3: 2
Case #4: 0
Case #5: 3'''

# Start from the end:
    # if +:
    #     pop and try again
    # else:
    #     pop, invert and try again

def getInput(doc):
    return open(doc, 'r').read().split('\n')

def convert(string):
    new = []
    for char in string:
        if char == '+':
            new.append(True)
        elif char == '-':
            new.append(False)
        else:
            print 'no bueno'
    return new

def invert(data):
    return [not item for item in array]

def moveNum(data):
    moves = 0
    if not data[-1]:
        moves = 1
        data = [not item for item in data]
    if len(data) != 1:
        data.pop()
        moves += moveNum(data)
    return moves

def run(doc):
    inp = getInput(doc)
    numTests = int(inp[0])
    tests = inp[1:]
    out = ''
    for i in range(numTests):
        out = out + '\nCase #' + str(i+1) + ': ' + str(moveNum(convert(tests[i])))
    output = open('output', 'w')
    output.write(out[1:])

run('B-large-practice.in')
