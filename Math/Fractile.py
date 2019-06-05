import math
# Input

'''5
-
-+
+-
+++
--+-'''

'''Case #1: 2
Case #2: 1
Case #3: IMPOSSIBLE
Case #4: 1 2
Case #5: 2 6'''

# Start from the end:
    # if +:
    #     pop and try again
    # else:
    #     pop, invert and try again

def getInput(doc):
    return open(doc, 'r').read().split('\n')

def convert(string):
    return [int(param) for param in string.split(' ')]

def check((k, c, s)):
    # print k, c, s
    if k == 1:
        return [1]
    elif k == s:
        return range(1,k+1)
    elif k > s*c:
        return 0
    else:
        indexes, num, done = [], 0, False
        while not done:
            index = 1
            for i in range(c):
                index += int(math.pow(k, c-i-1)) * num
                # print index, num
                if num == k - 1:
                    done = True
                if done:
                    num = 0
                else:
                    num += 1
            # print "index " + str(index)
            indexes.append(index)
        return indexes

    # Check 2nd of first pattern, then 4th of third pattern, etc.
    #   If G in place, it will result in G's in the next layer
    #   If L is in the place, then it will result in the same sequence
    #   Check multiple places with one
    # 3rd char of 2nd char of 1st char of first layer etc.
    #   if c > k, check that one
    #   elif k > s*c, impossible
    #   else check 3rd of 2nd of 1st then 6th of 5th of 4th, etc.

def toOut(array):
    if array == 0:
        return 'IMPOSSIBLE'
    else:
        out = ''
        for item in array:
            out += str(item) + ' '
        return out[:-1]

def run(doc):
    inp = getInput(doc)
    numTests = int(inp[0])
    tests = inp[1:]
    out = ''
    for i in range(numTests):
        out = out + 'Case #' + str(i+1) + ': ' + toOut(check(convert(tests[i]))) + '\n'
    output = open('output', 'w')
    output.write(out)

run('D-small-practice.in')
