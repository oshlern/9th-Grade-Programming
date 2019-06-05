from __future__ import division

inp = '''2
1
2'''
out = '''
Case #1: INSOMNIA
Case #2: 10
Case #3: 90
Case #4: 110
Case #5: 5076'''

def parse(inp):
     return inp.split('\n')[1:]
    # inp = inp.splice(0)

def findDigits(num):
    digits = []
    while num >= 1:
        newNum = num // 10
        digits += [num - newNum*10]
        num = newNum
    return digits

def addDigits(digits, addition):
    for digit in addition:
        if not digit in digits:
            digits.append(digit)
    return digits

def check(digits):
    for digit in range(10):
        if not digit in digits:
            return False
    return True

def solve(num):
    original, digits = num, []
    for i in xrange(1000):
        tempDigits = findDigits(num)
        digits = addDigits(digits, tempDigits)
        if check(digits):
            return str(num)
        num = num + original
    return 'INSOMNIA'

def run(inp):
    inp = parse(inp)
    out = ''
    for i in range(len(inp)-1):
        out = out + '\nCase #' + str(i+1) + ': ' + solve(int(inp[i]))
    return out

# print solve(1)
output = open('output', 'w')
output.write(run(open("A-large-practice.in", "r").read()))
