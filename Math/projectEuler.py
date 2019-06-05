# make code readable!
import math,re
# import primes to use from document
def getPrimes():
    primes=open("primes","r")
    primes=primes.read()
    # remove brackets
    primes=primes[1:len(primes)-2]
    # remove spaces
    primes=re.sub('[ ]','',primes)
    # split between commas to recreate array from string
    primes=primes.split(',')
    for i in range(len(primes)):
        primes[i]=int(primes[i])
    return primes
# primes=getPrimes()
primes=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]

# 1: how many multiples of 3 or 5 before 1000
    # 3*333*334/2+5*199*200/2-15*66*67/2

# 2: sum of even fibonacci up to 4 million
def evenFib(n):
    a=1
    o=1
    e=2
    sums=0
    while e<=n:
        sums+=e
        a=e+o
        o=a+e
        e=o+a
    print sums
    # evenFib(4000000)

# 3: prime factors
    # uses primes
def pfactor(n):
    global primes
    if n<2:
        print "invalid"
        return
    if n in primes:
        return n
    pfactors=[]
    i=-1
    divisor=0
    while i<len(primes)-1 and n!=1:
        i+=1
        divisor=primes[i]
        while n%divisor==0:
            pfactors+=[divisor]
            n=n/divisor
            print n
            print divisor
        print i
    while n!=1:
        divisor+=2
        while n%dvisor==0:
            pfactors+=[divisor]
            n=n/divisor
            print n
    return pfactors
    # print pfactor(600851475143)

# 4: palindrome from two 3-digit numbers
def findPal(m):
    def checkPal(n):
        s1=str(n)
        l=len(s1)
        s2=s1[int(math.floor(l/2)):]
        s1=s1[:int(math.ceil(l/2))]
        for i in range(len(s1)):
            if s1[i]!=s2[len(s1)-1-i]:
                return 0
        return 1
    for i in range(m):
        for j in range(m):
            pal=(999-i)*(999-j)
            if checkPal(pal):
                print pal
    # findPal(100)

# 5: divisible numbers
    # uses primes
def numDivBy(n):
    def generateFactors(n):
        factors=[]
        global primes
        for prime in primes:
            if prime>n:
                return factors
            factors+=[prime**int(math.floor(math.log(n)/math.log(prime)))]
    factors=generateFactors(n)
    print factors
    num=1
    for factor in factors:
        num=num*fctor
    return num
    # print(numDivBy(20))

# 6: sum square difference
    # (1+2+...+n)^2-(1^2+2^2+...+n^2)
def SquareSumDiff(n):
    def squareSum(n):
        return n*(n+1)*(2*n+1)/6
    def sumSquare(n):
        return (n*(n+1)/2)**2
    return sumSquare(n)-squareSum(n)
    # print SquareSumDiff(100)

# 7: primes
def createPrimes(n,kp):
    global primes
    k=1
    for i in range(kp):
        k*=primes[i]
    def checkpK(n):
        for i in range(kp):
            if n%primes[i]==0:
                return 0
        return 1
    numsCheck=[]
    for num in range(k):
        if checkpK(num):
            numsCheck+=[num]
    def checkp(n):
        for i in range(kp,len(primes)):
            if (n%primes[i])==0:
                return 0
        return 1
    # p=primes[kp]
    # for prime in range(kp,primes)
    #     if primes[prime]>k:
    for i in range(primes[-1]+2,n,k):
        for num in numsCheck:
            if checkpK(num+i):
                primes+=[num]
    return primes
# cPrimes=createPrimes(20000,1000)
# write primes on the prime doc
# if len(cPrimes)>len(primes):
#     primesOut=open("primes","w")
#     primesOut.write(str(cPrimes))
# print len(cPrimes)
# print cPrimes

# 8: Largest product in a series
def findProduct(length,number):
    numbers=[]
    # create an array of the digits
    for i in xrange(int(math.ceil(math.log(number)/math.log(10)))):
        if number==0:
            return sums
        m=number%10
        numbers+=[int(m)]
        number=(number-m)/10
    number=numbers
    # find indexes of the 0's
    zeros=[]
    for i in range(len(number)):
        if number[i]==0:
            zeros+=[i]
    largest=0
    # if there are 0's, don't calculate their product
    if len(zeros)>0:
        index=0
        for i in zeros:
            for j in range(index, i-length):
                # calculate product
                product=1
                for i in range(length):
                    product=product*number[j+i]
                # check if product is largest
                if product>largest:
                    largest=product
            index=i+1
        for j in range(index, len(number)-length):
            # calculate product
            product=1
            for i in range(length):
                product=product*number[j+i]
            # check if product is largest
            if product>largest:
                largest=product
    else:
        for j in range(len(number)-length):
            # calculate product
            product=1
            for i in range(length):
                product=product*number[j+i]
                # check if product is largest
            if product>largest:
                largest=product
    return largest
# print findProduct(13,7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450530420752963450)

# 9: Special Pythagoraean Triplet
    # a^2+b^2=c^2
    # a+b+c=n
    # solving for c and substituting and solving for b in terms of a we get:
    # n^2-2n*a-2n*b+2a*b=0
    # b = n*(a-n/2)/(a-n)
def findPythTrip(n):
    for a in range(1,n):
        for b in range(1,n-a):
            c=n-a-b
            if a**2+b**2==c**2:
                return (a,b,c)
# print findPythTrip(1000)

# 10: Sum primes
def sumPrimes(n):
    global primes
    def checkp(n):
        for i in range(len(primes)):
            if n%primes[i]==0:
                return 0
        return 1
    createPrimes(n,n/100)
    # for num in range(primes[-1]+2,n,2):
    #     if checkp(num):
    #         primes+=[num]
    sumP=0
    for prime in primes:
        if prime>n:
            return sumP
        sumP+=prime
    return sumP
# print sumPrimes(1000)

def gridProduct(grid, n):
    if len(grid)<n:
        if len(grid[0])<n:
            print 'you\'re bad'
            return 0
    def right(i, j):
        if j+n>len(grid[0]): return 0
        product = 1
        for k in range(n):
            product *= grid[i][j+k]
        return product
    def down(i, j):
        if i+n>len(grid): return 0
        product = 1
        for k in range(n):
            product *= grid[i+k][j]
        return product
    def dtl(i, j):
        if j+n>len(grid[0]) or i+n>len(grid[0]): return 0
        product = 1
        for k in range(n):
            product *= grid[i+k][j+k]
        return product
    def dtr(i, j):
        if j-n>0 or i-n>0: return 0
        product = 1
        for k in range(n):
            product *= grid[i-k][j-k]
        return product
    largest = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            product = right(i,j)
            if product > largest:
                largest = product
            product = down(i,j)
            if product > largest:
                largest = product
            product = dtr(i,j)
            if product > largest:
                largest = product
            product = dtl(i,j)
            if product > largest:
                largest = product
    return largest
grid = [[8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8],
    [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0],
    [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65],
    [52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91],
    [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
    [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
    [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
    [67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21],
    [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
    [21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95],
    [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92],
    [16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57],
    [86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
    [19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40],
    [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
    [88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
    [4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36],
    [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16],
    [20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54],
    [1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]]
# print gridProduct(grid, 4)
# 14: Long Collatz Sequence
values=[1]
methods=[0]
def cSequence(n):
    global values, methods
    longest=[0,1]
    def cStep(i):
        global values, methods
        if i in values:
            return methods[values.index(i)]
        else:
            nextStep=0
            if i%2==0:
                nextStep=i/2

            else:
                nextStep=3*i+1
            c=cStep(nextStep)+1
            methods+=[c]
            values+=[i]
            return c
    for i in range(2,n):
        c=cStep(i)
        if c>longest[0]:
            longest=[c,i]
    return longest
# print cSequence(100000)
# for i in range(len(values)):
#     print str(values[i])+": "+methods[i]


    # branch from 1
    # label evens and odds (maybe)
    # quit if over n
    # fin the longest one
# 16: power of 2 digit sum
def powerSum(n):
    def sumf(x):
        sums=0
        for i in xrange(int(math.ceil(math.log(x)/math.log(10)))):
            if x==0:
                    return sums
            m=x%10
            sums+=m
            x=(x-m)/10
        return sums
    # for i in range(1001):
    #     print "2^"+str(i)+": "+str(sumf(2**i))
    print "2^"+str(n)+": "+str(sumf(2**n))
# powerSum(1000)

# 25
# def fibDigit(n):

def makeFibs(n):
    num = 1
    a = 1
    b = 1
    def length(num):
        i = 0
        while num >= 1:
            num /= 10
            i += 1
        return i
    while length(a) != n:
        a, b = b, a + b
        num += 1
    return num
# print makeFibs(1000)

# 29
def distinctPowers(n):
    nums = range(2, n+1)
    powers = []
    def generatePowers(num, n):
        powers = []
        power = num
        for i in range(1, n):
            power *= num
            powers.append(power)
        return powers
    def generatePowersToN(num, n):
        powers = []
        power = num
        while power <= n:
            powers.append(power)
            power *= num
        return powers
    while len(nums) > 0:
        print nums
        powers += generatePowers(nums[0], n)
        print generatePowers(nums[0], n)
        for num in generatePowersToN(nums[0], n):
            nums.remove(num)
    return powers
print distinctPowers(5)


# 34
def digitFactorial():
    def digits(num):
        digits = []
        while num >= 1:
            digits += [num%10]
            num /= 10
        return digits
    def findLim():
        limit = 0
        # while True:
            # if limit > len(digits(9! * limit)):
                # return limit - 1
            # limit += 1
    limit = findLimit()
    num = [0]*limit
    for i in len(num):
        uselessVar = 1

# 47
def distinctPrimeFactors(n):
    num = n
    nums = []
    for i in range(n):
        nums += []

    while True:
        for i in range(1,n):
            num[i] = num[i-1]
        num[0] = factors

# 48
def selfPowers(n,d):
    s = 0
    for num in range(1,n+1):
        product = 1
        for i in range(num):
            product *= num
            product = product%d
        s += product
        s = s%d
    return s
# print selfPowers(1000, 10000000000)


# def digits(num):
#     digits = []
#     d = 0
#     while num:
#         d, num = num % 10, num // 10
#         digits += [d]
#     return digits
# print digits(1247234765)
# 248
def factorialDigits(m):
    global sfs#, sgs
    sfs = {}
    fs = []
    for n in range(10):
        fs += [math.factorial(n)]
    print fs
    def digits(num):
        digits = []
        d = 0
        while num:
            d, num = num % 10, num // 10
            digits += [d]
        return digits
    # def digitsStr(num):
    #     digits = []
    #     for char in str(num):
    #         digits += [int(char)]
    #     return digits
    def f(n):
        s = 0
        for digit in n:
            s += fs[digit]
        return s
    def sf(n):
        return sum(digits(f(n)))
    def nsf(n,fs):
        s = 0
        sn = 0
        while n:
            sn = sn + fs[n%10]
            n = n // 10
        while sn:
            s = s + sn%10
            sn = sn // 10
        return s
    def g(i):
        global sfs#, sgs
        p = partitions(i)
        # factor(p) = 2*3*4+2*3+2*3*4*5*6
        #             = 2*3*(5)*(4*6+1)#to find factorials
        if i in sfs:
            n = sfs[i]
            print str(i) + ' - found at: ' + str(n)
            return n
        else:
            n = len(sfs)-1
            #sgsL = len(sgs)
            currentSF = 0
            s = 0
            while s != i:

                if n[0] == 9:
                    n[0] = 0
                    # return [n[0]] +
                else:
                    n[0] = n + 1
                n = n+1
                s=0
                tn = n
                while tn:
                    s, tn = s + fs[tn%10], tn // 10
                tn, s = s, 0
                while tn:
                    s, tn = s + tn%10, tn // 10
                if not s in sfs:
                    sfs[s] = n
            # while currentSF != i:
            #     n+=1
            #     currentSF = sf(n)
            #     sfs += [currentSF]
            #     print currentSF
                    # sgs += n
            print str(i) + ' - found at: ' + str(n)
            return n
    def sg(i):
        return sum(digits(g(i)))
    total = 0
    for i in range(1,m+1):
        total += sg(i)
    return total
# def factorialDigits(m):
#     global sfs#, sgs
#     sfs = {}
#     fs = []
#     for n in range(10):
#         fs += [math.factorial(n)]
#     print fs
#     def digits(num):
#         digits = []
#         d = 0
#         while num:
#             d, num = num % 10, num // 10
#             digits += [d]
#         return digits
#     # def digitsStr(num):
#     #     digits = []
#     #     for char in str(num):
#     #         digits += [int(char)]
#     #     return digits
#     def f(n):
#         s = 0
#         for digit in digits(n):
#             s += fs[digit]
#         return s
#     def sf(n):
#         return sum(digits(f(n)))
#     def nsf(n,fs):
#         s = 0
#         sn = 0
#         while n:
#             sn = sn + fs[n%10]
#             n = n // 10
#         while sn:
#             s = s + sn%10
#             sn = sn // 10
#         return s
#     def g(i):
#         global sfs#, sgs
#         if i in sfs:
#             n = sfs[i]
#             print str(i) + ' - found at: ' + str(n)
#             return n
#         else:
#             n = len(sfs)-1
#             #sgsL = len(sgs)
#             currentSF = 0
#             s = 0
#             while s != i:
#                 n = n+1
#                 s=0
#                 tn = n
#                 while tn:
#                     s, tn = s + fs[tn%10], tn // 10
#                 tn, s = s, 0
#                 while tn:
#                     s, tn = s + tn%10, tn // 10
#                 if not s in sfs:
#                     sfs[s] = n
#             # while currentSF != i:
#             #     n+=1
#             #     currentSF = sf(n)
#             #     sfs += [currentSF]
#             #     print currentSF
#                     # sgs += n
#             print str(i) + ' - found at: ' + str(n)
#             return n
#     def sg(i):
#         return sum(digits(g(i)))
#     total = 0
#     for i in range(1,m+1):
#         total += sg(i)
#     return total
    # to find sg(i), split i into partitions and make a number with digits as the elements of the partition
    # only use numbers that add up to the wanted amount
# print factorialDigits(150)
