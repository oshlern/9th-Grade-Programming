import random

# no 2 digits the same
length = 3
digits = 10
end = 100

def strat(myNums, results):
    guessNum = len(myNums)
    def guess():
        num = []
        for i in range(length):
            # num += [digits[i%len(digits)]]
            num += [random.randint(0, digits)]
        return num
    if guessNum == 0:
        return guess()
    return guess()

def generate(length, digits):
    num = []
    for i in range(length):
        num += [random.randint(0, digits)]
    return num

def check(guess, num):
    result = {'right': 0, 'place': 0, 'wrong': 0}
    for digit in num:
        if digit in guess:
            if num.index(digit) == guess.index(digit):
                result['right'] += 1
            else:
                result['place'] += 1
        else:
            result['wrong'] += 1
    return result

# check for appropriate strat result
def error():
    if type(num) != list:
        print "Must return an array"
        return 1
    if len(num) != length:
        print "Array must be of length: " + str(length)
        return 1
    for digit in num:
        if type(digit) != int:
            print "Items of array must be integers"
            return 1
        if not digit in range(digits):
            print "Digits must be between 0 - " + str(digits-1)
    return 0

def run(length, digits, end):
    num = generate(length, digits)
    if error():
        return 0
    myNums = []
    results = []
    for i in range(end):
        guess = strat(myNums, results)
        result = check(guess, num)
        if result['right'] == length:
            return i
        results += [result]
        myNums += [guess]

print run(length, digits, end)
