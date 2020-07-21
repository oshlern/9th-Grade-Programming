# Spanish: 4 and 6 loop or 5 or 3
# Hebrew: 4 in masculine form, 4 and 5 loop in feminine form
# Swedish: 3 or 4
# Dutch: 4
# Russian: everything leads to 4 and 7 loop other than 2 and 3 which stop at 3
# Italian: 3
# German: 4
# Roman Numerals: 1, 2, or 3

def toDigits(num):
    digits = []
    while num != 0:
        digit = num % 10
        digits.append(digit)
        num = (num-digit)/10
    return digits

vocab = [["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"],
    ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"],
    "twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety", "hundred"]
vocabLarge = ["", "thousand", "million", "billion", "trillion", "quadrillion"]

numbers = {}
# 21,655
def toLength(words):
    if type(words) == list:
        for i in range(len(words)):
            words[i] = toLength(words[i])
    elif type(words) == str:
        words = len(words)
    return words
length = toLength(vocab)
lengthLarge = toLength(vocabLarge)
def numLength(digits, l):
    # print digits, l
    if len(digits) == 0:
        return "error"
    if l == 0:
        if digits[0] != 0:
            return length[0][digits[0]]
        return 0
    if l == 1:
        out = length[digits[1]]
        if type(out) == list:
            return out[digits[0]]
        return out + length[0][digits[0]]
    if l == 2:
        out = length[0][digits[2]]
        if digits[2] != 0:
            out += 7
        # print out, "ew"
        return out + numLength(digits[:2], 1)
    size = l/3
    # print "x: ", size
    # print "SO", numLength(digits[:size*3], size*3-1)
    return numLength(digits[size*3:], l-size*3) + lengthLarge[size] + numLength(digits[:size*3], size*3-1)

def findLength(num):
    digits = toDigits(num)
    l = numLength(digits, len(digits)-1)
    numbers[num] = l

def path(num):
    out = [num]
    while num != 4:
        num = findLength(num)
        out += [num]
    return out

ones = length[0]
teens = length[1]
def pathLength(num):
    out = 0
    while num != 4:
        print num, "new"
        if num < 10:
            num = ones[num]
        elif num < 20:
            num = teens[num-10]
        else:
            print findLength(num)
            num = findLength(num)
        out += 1
    return out

# print findLength(23)
# print path(573341431)
print pathLength(573341431)
