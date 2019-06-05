# make functions to print fibonacci to find any f(n) = sum(i=1 to k)(f(n-i))
import re
import math

doc =  'DimFib'

def getFibs(doc):
    fib=open(doc,"r").read()
    # formatting
    fib = fib[2:-2]
    fib = fib.split('], [')
    for j in range(len(fib)):
        fib[j] = fib[j].split(', ')
        for k in range(len(fib[j])):
            if (fib[j][k][-1] == 'L'):
                fib[j][k] = fib[j][k][:-1]
            fib[j][k] = int(fib[j][k])
    return fib

def saveFibs(doc, nums):
    output = open(doc,"w")
    output.write(str(nums))

def fib(n, j):
    global fibs
    if (len(fibs)<=j):
        # add the appropriate amount of ones and the next number to every fib[i] until fib[j]
        for i in range(len(fibs), j+1):
            fibs += [([1] * i) + [i]]

    if (len(fibs[j])<=n):
        # add up elements to get new one
        fibs[j] += [2 * fib(n-1, j) - fib(n-j-1, j)]

    return fibs[j][n]

fibs = getFibs(doc)
# fibs = []
print fib(5001, 100)
saveFibs(doc, fibs)
