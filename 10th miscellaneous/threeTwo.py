import numpy as np
import math

def threeTwo(num):
    digits = [num]
    while num > 2:
        num = int(np.floor(num/3))
        digits[0] -= num*3
        num *= 2
        digits = [num] + digits
    return digits

def findNew(old, new, target):
    # target -= 1
    digits = [new, 0]
    length = 2
    nums = [[1], digits]
    count = old
    while length < target:
        digits[-2] += new
        count += old
        for i in range(length-1, 0, -1):
            if digits[i] >= old:
                # print digits[i]
                # num = int(np.floor(np.divide(digits[i], old)))
                num = int(math.floor(digits[i]/old))
                digits[i] -= num * old
                digits[i-1] += num * new
        if digits[0] >= old:
            # num = int(np.floor(np.divide(digits[0],old)))
            num = int(math.floor(digits[0]/old))
            digits[0] -= num * old
            digits = [num * new] + digits
            length += 1
            nums.append((length, count, digits))
            print count, length
    # print digits
    return nums

def findNewEfficient(old, new, target):
    # target -= 1
    digits = [new, 0]
    length = 2
    nums = [[1], digits]
    count = old
    while length < target:
        digits[-2] = np.add(digits[-2], new)
        count = np.add(count, old)
        for i in range(length-1, 0, -1):
            if digits[i] >= old:
                num = int(np.floor(np.divide(digits[i], old)))
                digits[i] = np.subtract(digits[i], np.multiply(num, old))
                digits[i-1] = np.add(digits[i-1], np.multiply(num, new))
        if digits[0] >= old:
            num = int(np.floor(np.divide(digits[0], old)))
            digits[0] = np.subtract(digits[0], np.multiply(num, old))
            digits = [np.multiply(num, new)] + digits
            length = np.add(length, 1)
            nums.append(count)
            print length, count, digits
    return nums

print findNew(3, 2, 100)
# print findNewEfficient(3, 2, 35)

# def findNew(target):
#     target -= 1
#     digits = [2] #leave off 1's
#     length = 1 #2
#     nums = [[2]]
#     while length < target:
#         digits[0] += 2
#         for i in range(length,1):
#             if digits[i] >= 3:
#                 num = int(np.floor(np.divide(digits[i],3)))
#                 digits[i] -= num*3
#                 digits[i-1] -= num*2
#         if digits[0] >= 3:
#             num = int(np.floor(np.divide(digits[0],3)))
#             digits[0] -= num*3
#             digits = [num*2] + digits
#             length += 1
#             nums.append(digits)
#         print digits
#     return nums

# print findNew(5)


# for i in range(100):
#     print threeTwo(i)
# print threeTwo(64)
