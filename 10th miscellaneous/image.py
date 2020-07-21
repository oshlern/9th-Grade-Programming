import cv2, math, binascii, base64
import numpy as np
from fractions import gcd

# simple decoding
# c = open('b64', 'r').read()
# # print c.decode('base64')
# print 'eW91ciB0ZXh0'.decode('base64')
# C = c.split('\n')
# c = ''
# for text in C:
# 	c += text.decode('base64')
# for i in range(50):
# 	c = c.decode('base64')
# 	print len(c), c, '\n\n'

# finn stormtrooper
img = cv2.imread("/Users/oshlern/Downloads/stormtrooper.jpg")
real = cv2.imread("/Users/oshlern/Downloads/finn.jpg")
size = img.shape
# print np.subtract(size, real.shape)
print size, real.shape
colors = cv2.split(real)
for i in range(len(colors)):
	cv2.imshow(str(i), colors[i])
real = cv2.resize(real, size[:2])
# x = real == img
# print False in x
# print real, img
diff2 = np.subtract(real, img)
diff = np.subtract(img, real)
# print np.amax(diff), np.amin(diff)
# print np.amax(diff2), np.amin(diff2)
# cv2.imshow("img", img)
# cv2.imshow("real", real)
# cv2.imshow("diff", diff)
# cv2.imshow("diff2", diff2)
# diffie
ga = 421049228295820
gb = 105262307073955
p = 442101689710611

def is2Pow(n):
	for i in range(1000):
		if n == 1:
			return i
		if n%2 == 0:
			n/=2
		else:
			return False

def findPow(n, mod):
	num = 2
	for i in range(1, 10000000000):
		if i % 10000 == 1:
			print i
		if num == n:
			return i
		num = num*2 % mod
	print "RIP"


# print is2Pow(64)
# for i in range(1000000):
# 	isPow = is2Pow(gb + i*p)
# 	if isPow:
# 		print isPow, i
# print "starting"
# print findPow(ga, p)


# perfect encryption
# string = open('info', 'r').read()
# print len(string)
# letters = []
# for letter in string:
# 	if not letter in letters:
# 		letters += [letter]
# print letters, len(letters)
# print len('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
# for l in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789':
# 	if not l in letters:
# 		print l
# 	else:
# 		letters.remove(l)
# print letters
# library
zs = [1]
os = [1]
def o(n):
	global os
	if len(os) > n:
		return os[n]
	else:
		new = o(n-1) + z(n-1)
		os += [new]
		return new

def z(n):
	global zs
	if len(zs) > n:
		return zs[n]
	else:
		new = o(n-1) + o(n) #o(n-1)*2 + z(n-1)
		zs += [new]
		return new

# inp = input()

# print z(inp)%mod


def o(n):
	# os = [1, 3]
	lastA, lastB = 3, 1
	for _ in xrange(n-1):
		lastA, lastB = lastA*2 + lastB, lastA
	return lastA



	# num = 1
	# for i in xrange(e):
	# 	num = np.multiply(num,b)
	# 	if num > n:
	# 		num = np.mod(num, n)
	# return num

# print pow(3, 141500000, 1892)
# n = 500000
# print powmod(3**n, 141500000/n, 1892)
# print powmod(3, 141500000, 1892)

# mod = (10**9 + 7)*2
# l1 = 1 + np.sqrt(2)
# l2 = 1 - np.sqrt(2)

# def powmod(b, e, n):
# 	x, y = 1, b; 
# 	while e > 0:
# 		if e%2 == 1:
# 			x = np.mod(np.multiply(x,y), n)
# 		y = np.mod(np.square(y), n)
# 		e = np.divide(e, 2)
# 	return x%n;

# def o(n):
# 	if n%2 == 1:
# 		n1 = np.mod(np.multiply(powmod(l1,n-1,mod), l1), mod)
# 		n2 = np.mod(np.multiply(powmod(l2,n-1,mod), l1), mod)
# 	else:
# 		n1 = powmod(l1,n,mod)
# 		n2 = powmod(l2,n,mod)
# 	# print n1, n2
# 	return int(round(np.divide(np.add(n1, n2), 2)))%(mod/2)

# n = input()
# print o(n+1)
# print o(2**14)
# print zs(input)
# print o(400)

# print os
# print zs

# Fzz Buzzz
# number = input()
# DONT USE: if, in, while 
# USE: map, def, 
# number = 11
# Range = range(1, number + 1)
# def prntN(N):
# 	n = N/15
# 	remander = N - n
# 	RANGE = range(1,n+1)
# 	# PRINT?
# 	map(lambda x: prntBunch(x), RANGE)

# def prntBunch(n):
# 	prnt(n)
# 	prnt(n+1)
# 	prnt('Fzz')
# 	prnt(n+3)
# 	prnt('Buzz')
# 	prnt('Fzz')
# 	prnt(n+6)
# 	prnt(n+7)
# 	prnt('Fzz')
# 	prnt('Buzz')
# 	prnt(n+10)
# 	prnt('Fzz')
# 	prnt(n+12)
# 	prnt(n+13)
# 	prnt('FzzBuzz')

# # PRINT?
# map(lambda x: prnt(x), Range)
# for j in range(1,number+1):
# 	s = ""
# 	if index%3==0:
# 		string += "Fizz"
# 	if index%5==0:
# 		string += "Buzz"
# 	if string == "":
# 		string = index
# 	print string
# Array of nums and strs
# Take indeces


# Hekkerman
# original = cv2.imread("/Users/oshlern/Downloads/hekkerman.jpg")
# real = cv2.imread("/Users/oshlern/Downloads/hekkerman2.jpg")
# # print original
# print real.shape, original.shape

# real = cv2.resize(real, (original.shape[1], original.shape[0]))
# print real.shape, original.shape

# cv2.imshow('real', real)
# cv2.imshow('orig', original)
# diff1 = np.subtract(original, real)
# diff2 = np.subtract(real, original)
# print np.amin(diff1), np.amax(diff1)
# print np.amin(diff2), np.amax(diff2)
# diff = np.subtract(diff1, diff2)
# cv2.imshow('diff1', diff1)
# cv2.imshow('diff2', diff2)
# cv2.imshow('diff', diff)
# cv2.imwrite('hekkermanDiff.jpg', diff)


# file1 = open('file1', 'r').read()
# file2 = open('file2', 'r').read()
# f1 = [ord(char) for char in file1]
# f2 = [ord(char) for char in file2]
# diff = np.subtract(f1,f2)
# # print np.average(diff)
# Diff = [num for num in diff if num != 0]
# print Diff
# Diff = np.subtract(Diff, np.amin(Diff))
# print Diff
# string = ''
# for num in Diff:
#     if num != 0:
#         # print num
#         string += chr(abs(num))
# print string

# diffie?
# gpa = 421049228295820
# gpb = 105262307073955
# p=442101689710611
# print pow(gpa, gpb, p)
# inp = raw_input()
# print "ioashd"
# print inp
# print type(inp)
# inp = raw_input()
# print "ioashd"
# print inp
# print type(inp)

# 0(n) = 2*1(n-1) + 0(n-1)
# 1(n) = 1(n-1) + 0(n-1)
# 
# 0(1) = 1
# 1(1) = 1

# 0: 1, 3, 7, 17, 41, 99
# 1: 1, 2, 5, 12, 29, 70

# 1, 2n, 4*(2n-3) + (2n-4)(2n-4), ............(4*(2n-6)*3*(3*(2n))

# RSA
p = 34200289574997044861430451448634231862429002919124420593723635048303773635074137
q = 31807401424075584497317842931435232917687722537341564055279629294106704843161747
e = 65537
c = 115546064239183991344958991096332743131210014541485588209772444848628113389891314495332325684527648258157091063446128518861645829611966485327534539686142390890

def extended_gcd(aa, bb):
	lastremainder, remainder = abs(aa), abs(bb)
	x, lastx, y, lasty = 0, 1, 1, 0
	while remainder:
		lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
		x, lastx = lastx - quotient*x, x
		y, lasty = lasty - quotient*y, y
	return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)

def lcm(a, b):
	return np.divide(np.multiply(a,b), gcd(a,b))

def modInv(a, m):
	g, x, y = extended_gcd(a, m)
	if g != 1:
		raise Exception('modular inverse does not exist')
	else:
		return x % m

def crt(m, a): # tuples 3 long
	M = reduce(mul, m) # the product of m elements
	m_i = [M / item for item in m]
	b = map(mod, m_i, m)
	g, k, l = map(egcd, b, m)
	g, k, l = zip(g, k, l) # transpose g, k and l arrays
	t = map(mod, k, m)
	e = map(mul, m_i, t)

	x_sum = sum(map(mul, a, e))
	x = x_sum % M

	return x

def factorize(n):
	if n%2==0:
		return 2
	if n%3==0:
		return 3
	if n%5==0:
		return 5
	m = int(math.sqrt(n))
	print "sqrt", m
	i = 7
	while i <= m:
		if n%i == 0:
			return i
		if n%(i+4) == 0:
			return i+4
		if n%(i+6) == 0:
			return i+6
		if n%(i+10) == 0:
			return i+10
		if n%(i+12) == 0:
			return i+12
		if n%(i+16) == 0:
			return i+16
		if n%(i+22) == 0:
			return i+22
		if n%(i+24) == 0:
			return i+24
		if i%30000000 == 7:
			print i
		i += 30
	print "RIPPP"
	# not Fast ENOUGH
	# np is really slow


# n = np.multiply(p,q)
# lam = lcm(p-1, q-1)
# # lam = (p-1)*(q-1)
# print lcm(p-1, q-1) - lam

# d = modInv(e, lam)
# m = pow(c, d, n)
# # print m, "as"
# b = bin(m)
# print b
# print n
# print d

def numToAscii(m, nchars):
	print ''.join(chr((m>>8*(nchars-byte-1))&0xFF) for byte in range(nchars))


# RSA 2
n = 617949289737338523885658388727172491572371
e = 65537
c = 377948795377301124958325120712434416323788

p = 779403844637773725049
q = 792848654761934281579

# n = np.multiply(p,q)
# lam = lcm(p-1, q-1)
# d = modInv(e, lam)
# m = pow(c, d, n)
# print pow(m, e, n) - c
# print numToAscii(m, 1000)

# RSA 3
#{N : e : c} {0x27335d21ca51432fa000ddf9e81f630314a0ef2e35d81a839584c5a7356b94934630ebfc2ef9c55b111e8c373f2db66ca3be0c0818b1d4eda7d53c1bd0067f66a12897099b5e322d85a8da45b72b828813af23L : 0x10001 : 0x9b9c138e0d473b6e6cf44acfa3becb358b91d0ba9bfb37bf11effcebf9e0fe4a86439e8217819c273ea5c1c5acfd70147533aa550aa70f2e07cc98be1a1b0ea36c0738d1c994c50b1bd633e3873fc0cb377e7L}
n = 0x27335d21ca51432fa000ddf9e81f630314a0ef2e35d81a839584c5a7356b94934630ebfc2ef9c55b111e8c373f2db66ca3be0c0818b1d4eda7d53c1bd0067f66a12897099b5e322d85a8da45b72b828813af23L
e = 0x10001
c = 0x9b9c138e0d473b6e6cf44acfa3becb358b91d0ba9bfb37bf11effcebf9e0fe4a86439e8217819c273ea5c1c5acfd70147533aa550aa70f2e07cc98be1a1b0ea36c0738d1c994c50b1bd633e3873fc0cb377e7L
n = 11721152358236061520231546547637479326600733856476942783391651261161073932522251528868410691769508664585409225554242334270429894938143275720784205110462278896087432260439082955593874915727686637956899
# no common divisors with old n's
# UNMODDED@ (*#&*T^@&#(*))
#hex qr
# trueQR = cv2.imread("/Users/oshlern/Downloads/trueQR.png")
# qr1 = cv2.imread("/Users/oshlern/Downloads/qr1.png")
# qr2 = cv2.imread("/Users/oshlern/Downloads/qr2.png")
# qr3 = cv2.imread("/Users/oshlern/Downloads/qr3.png")
# qr4 = cv2.imread("/Users/oshlern/Downloads/qr4.png")
# diff1 = np.subtract(trueQR, qr1)
# diff2 = np.subtract(trueQR, qr2)
# diff3 = np.subtract(trueQR, qr3)
# diff4 = np.subtract(trueQR, qr4)
# cv2.imshow('1',diff1)
# cv2.imshow('2',diff2)
# cv2.imshow('3',diff3)
# cv2.imshow('4',diff4)
# diff = np.subtract(diff1, diff2)
# cv2.imshow('diff', diff)
# print np.amax(diff)
# print np.amax(np.subtract(qr1,qr2))

# RSA 4
p= 13013195056445077675245767987987229724588379930923318266833492046660374216223334270611792324721132438307229159984813414250922197169316235737830919431103659
q= 12930920340230371085700418586571062330546634389230084495106445639925420450591673769061692508272948388121114376587634872733055494744188467315949429674451947

e= 100

C= 2536072596735405513004321180336671392201446145691544525658443473848104743281278364580324721238865873217702884067306856569406059869172045956521348858084998514527555980415205217073019437355422966248344183944699168548887273804385919216488597207667402462509907219285121314528666853710860436030055903562805252516

# e isn't coprime, gcd(e, lam) = 2
# D + 1/e (real 1/e? there is no inverse)
lam = 84136294323385483438649994124974693353865320388360264700465956188343934636944408638507451238954464709433591838764407839288237734970825038493294620488643756765016000966811684948309440760973569390322399594194164755294352213590435561770349469894496835532577115034837769530080997134347370344650507094178532909234
# print lam % 5, "ASD"
# print pow(e, (lam-1)/2, lam)%8

# Find sqrt(C) mod n by finding sqrt(C) mod p,q and using chinese remainder theorem
# c = sqrt(sqrt(C)) actually
# Find d for e=25 (e^-1 mod lam)
# take c^d mod n
# d = np.true_divide(lam + 1, e)
# d, remainder = int(math.floor(d)), d - math.floor(d)
# m = pow(c, d, n)
# print m
# print "Done"
# print numToAscii(m, 10000)
# print modInv(e, lam)

# fzz buzz 2 - no elses. ? is like if? i is iterated?

# QR
def pxlTovVal(img):
	avg = np.average(img)
	if avg < 255 - avg:
		return 0
	else:
		return 1

def imageToQR(src, dipsX, dispY, pxlSize):
	shp = src.shape
	img = src[dispX:shp[0]-dispX, dispY:shp[1]-dispY]
	shp = img.shape
	numX = np.ciel(np.divide(shp[0],pxlSize))
	numY = np.ciel(np.divide(shp[1],pxlSize))
	qr = np.zeros((numX, numY))
	for i in range(numX):
		for j in range(numY):
			pxl = img[i*pxlSize:(i+1)*pxlSize, j*pxlSize:(j+1)*pxlSize]
			qr[i,j] = pxlTovVal(pxl)

def qrToImage(qr, pxlSize):
	shp = qr.shape
	img = np.multiply(shp, pxlSize)
	for i in range(shp[0]):
		for j in range(shp[1]):
			img[i*pxlSize:(i+1)*pxlSize, j*pxlSize:(j+1)*pxlSize] = np.multiply(np.ones((pxlSize, pxlSize)), qr)
	return img



#marriage

# def parsePref(file):
# 	names = []
# 	file = open(file,"r").read()
# 	people = file.split('\n')
# 	if len(people[-1]) == 0:
# 		people.pop()
# 	for i in range(len(people)):
# 		person = people[i].split(', ')
# 		temp = person[0].split(' ')
# 		person[0] = temp[1]
# 		names += [temp[0]]
# 		person = [int(num)-1 for num in person]
# 		people[i] = person
# 	return people, names
# males, maleNames = parsePref('malesData')
# females, femaleNames = parsePref('femalesData')
# # print maleNames
# # males = parsePref('males1')
# # females = parsePref('females1')
# numMales = len(males)
# numFemales = len(females)
# engagedM = [-1 for i in range(numMales)]
# engagedF = [-1 for i in range(numFemales)]
# engagedRankM = [-1 for i in range(numMales)]
# engagedRankF = [-1 for i in range(numFemales)]
# # print males, females
# def proposalRound():
# 	notFinished = False
# 	for male in range(numMales):
# 		if engagedM[male] == -1:
# 			notFinished = True
# 		else:
# 			continue
# 		female = males[male].pop(0) #male proposes to top choice
# 		for index in range(len(females[female])): #loop through female's interests
# 			if females[female][index] == male: #if male in interests
# 				if engagedF[female] != -1:
# 					engagedM[engagedF[female]] = -1
# 					engagedRankM[engagedF[female]] = -1
# 					notFinished = True
# 				engagedF[female] = male #get engaged
# 				engagedM[male] = female
# 				engagedRankF[female] = index 
# 				engagedRankM[male] = numFemales - len(males[male]) - 1
# 				females[female] = females[female][:index] #remove any worse choices from female
# 				break
# 	return notFinished

# def marriage():
# 	notFinished = True
# 	i =0
# 	while notFinished:
# 		# print "ROUND ", i
# 		notFinished = proposalRound()
# 		i+=1
# marriage()
# first = [engagedM, engagedF, engagedRankM, engagedRankF]

# males, a = parsePref('femalesData')
# females, a = parsePref('malesData')
# numMales = len(males)
# numFemales = len(females)
# engagedM = [-1 for i in range(numMales)]
# engagedF = [-1 for i in range(numFemales)]
# engagedRankM = [-1 for i in range(numMales)]
# engagedRankF = [-1 for i in range(numFemales)]
# marriage()
# second  = [engagedM, engagedF, engagedRankM, engagedRankF]
# rand = np.random.randint(numMales)
# print rand == first[0][first[1][rand]]

# pairs = []
# for male in range(numMales):
# 	if first[1][male] == second[0][male]:
# 		# pair = (maleNames[first[1][male]], femaleNames[male])
# 		pair = '(' + str(maleNames[first[1][male]]) + ',' + str(femaleNames[male]) + ')'
# 		pairs += [pair]
# 		print pair
# pairs = sorted(pairs)
# string = ''
# for pair in pairs:
# 	string += pair
# print string
# print np.average(first[2]), np.average(second[2])
# print np.average(first[3]), np.average(second[3])
# # print male, second[0][male]

# # proposalRound()
# # print "engagedM", engagedM
# # print "engagedF", engagedF
# # print "engagedRankM", engagedRankM
# # print "engagedRankF", engagedRankF







# #unzip first
# names = [""]
# images = []
# for name in names:
# 	images += [cv2.imread(name)]


# #QR2
# image = cv2.imread("/Users/oshlern/Downloads/013fe9411d3a9ca12cc846b637dd7be9df7aef8d_qr2.bmp")
# image = image[:,:,0]
# shp = image.shape
# for i in range(shp[0]):
# 	for j in range(shp[1]):
# 		if 40 < i < 120:
# 			if 40< j < 120 or shp[1]-40 > j > shp[1] - 120:
# 				continue
# 		elif shp[0]-40 > i > shp[0]-120 and 40 < j < 120:
# 			continue
# 		elif shp[0]-80> i > shp[0]-130 and shp[0]-80> j > shp[0]-130:
# 			continue
# 		if image[i,j] == 0:
# 			image[i,j] = 255
# 		elif image[i,j] == 255:
# 			image[i,j] = 0
# 		else:
# 			print image[i,j], i, j

# # cv2.imshow('qr',image)

# #QR
# image = cv2.imread("/Users/oshlern/Downloads/55b2063cb31834298a8ec44a518d93f5359840b7_qr1.bmp")
# shp = image.shape[:2]
# print shp

# # cv2.imshow(image)
# channels = cv2.split(image)
# r,g,b = channels[0], channels[1], channels[2]
# R,G,B = r,g,b
# # R,G,B = np.zeros(shp), np.zeros(shp), np.zeros(shp)
# index = 0
# for mat,MAT in zip([r,g,b],[R,G,B]):
# 	for i in range(shp[0]):
# 		for j in range(117) + range(shp[1]-117, shp[1]):
# 			if mat[i,j] == 1:
# 				# print i,j, "1"
# 				MAT[i,j] = 255
# 			elif mat[i,j] == 254:
# 				# print i,j
# 				MAT[i,j] = 0
# 			# if mat[i,j] != 0 and mat[i,j] != 255:
# 			# 	# print mat[i,j]
# 			# 	MAT[i,j] = 255
# 			# else:
# 			# 	MAT[i,j] = 0
# 	# MAT = cv2.cvtColor(MAT, cv2.COLOR_GRAY2BGR)
# 	# print type(MAT)
# 	# cv2.imshow(str(index), MAT)
# 	index+=1


# image = cv2.imread("/Users/oshlern/Downloads/easyctfcolors.png")
# channels = cv2.split(image)
# r,g,b = channels[0], channels[1], channels[2]
# cv2.imshow('g', r)
# print type(r)
# print r.shape
# print np.amax(r)
# # for row in r:
# # 	for i in row:
# # 		print chr(i)
# # print r, g, b
# def toBin(mat):
# 	out = []
# 	for row in mat:
# 		out += [[0 if element == 0 else 1 for element in row]]
# 	return np.array(out)

# def arrToBase(digits, base=2): #takes in array
# 	num = 0
# 	m = math.pow(base,len(digits)-1)
# 	for digit in digits:
# 		num += m * digit
# 		m /= base
# 	return int(num)

# def takeFirst(mat):
# 	digits = []
# 	for col in mat:
# 		digits += [col[0]]
# 	return np.array(digits)

# R = takeFirst(toBin(r).T)
# G = takeFirst(toBin(g).T)
# B = takeFirst(toBin(b).T)
# # print R
# # print G
# # print B
# # print len(R)
# n = 43
# for i in range(0,len(R),n):
# 	s = []
# 	for x in R[i:i+n]:
# 		s += [x]
# 	# print s
# # for i in range(len(R)/8-1):
# # 	# print R[i:i+8]
# # 	num = arrToBase(R[i:i+8])
# # 	print num, chr(num)


# def toAsc(mat):
# 	string = ''
# 	for row in mat:
# 		isOn = [1 if a != 0 else 0 for a in row]
# 		print isOn
# 		num = arrToBase(isOn)
# 		print num
# 		char = chr(num)
# 		print char
# 		string += char
# 	return string


# # print arrToBase([1,1,0,1])


# # cv2.imshow('r',channels[0])
# # cv2.imshow('g',channels[1])
# # cv2.imshow('b',channels[2])
cv2.waitKey(0)
cv2.destroyAllWindows()