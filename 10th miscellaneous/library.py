import math
from decimal import *
getcontext().prec = 10000
root_2 = math.sqrt(2)
# number = input()
mod = 10**9 + 7
def luc(number):
	num_1 = ((1+root_2)**number - (1-root_2)**number) / root_2
	num_2 = ((1+root_2)**number + (1-root_2)**number) / 2
	print num_1, num_2
	return (num_2+num_1) % mod# import math


# x - y / root_2
# x + y / 2
# x+x*root_2 - y+y*root_2 / root_2 * 2
# x+x*root_2 + y+y*root_2 / 2 * 2
# x+x*root_2 - y+y*root_2 / root_2 * 2
# x+x*root_2  * (1 + root_2) + y+y*root_2 ((1 - root_2))
# from decimal import *
# getcontext().prec = 100
# mod = (10**9 + 7)
# mod2 = mod*2
# root_2 = math.sqrt(2)

# l1 = 1 + math.sqrt(2)
# l2 = 1 - math.sqrt(2)

# def powmod(b, e, n):
# 	x, y = 1, b; 
# 	while e > 0:
# 		if e%2 == 1:
# 			x = x*y % n
# 		y = pow(y, 2) % n
# 		e /= 2
# 	return x%n;

# def o(n):
# 	if n%2 == 1:
# 		n1 = powmod(l1,n-1,mod2) * l1 % mod2
# 		n2 = powmod(l2,n-1,mod2) * l2 % mod2
# 	else:
# 		n1 = powmod(l1,n,mod2)
# 		n2 = powmod(l2,n,mod2)
# 		# n1 = powmod(l1,n-2,mod) * l1 * l1 % mod
# 		# n2 = powmod(l2,n-2,mod) * l2 * l2 % mod
# 	# print n1, n2
# 	# return int(round((n1 + n2)/ 2))%(mod/2)
# 	# n1 = powmod(l1,n,mod2)
# 	# n2 = powmod(l2,n,mod2)
# 	# return ((n1 + n2)/ 2)%mod
# 	return ((n1 + n2)/ 2 + (n1 - n2)/ root_2)%mod


# def luc(n):
# 	num_1 = ((1+root_2)**n - (1-root_2)**n) / root_2
# 	num_2 = ((1+root_2)**n + (1-root_2)**n) / 2
# 	return num_2+num_1


# n = input()
# print o(n+1)
# import math
# mod = (10**9 + 7)*2
# l1 = 1 + math.sqrt(2)
# l2 = 1 - math.sqrt(2)

# def powmod(b, e, n):
# 	x, y = 1, b; 
# 	while e > 0:
# 		if e%2 == 1:
# 			x = x*y % n
# 		y = pow(y, 2) % n
# 		e /= 2
# 	return x%n;

# def o(n):
# 	if n%2 == 1:
# 		n1 = powmod(l1,n-1,mod) * l1 % mod
# 		n2 = powmod(l2,n-1,mod) * l2 % mod
# 	else:
# 		n1 = powmod(l1,n,mod)
# 		n2 = powmod(l2,n,mod)
# 	# print n1, n2
# 	return int(round((n1 + n2)/ 2))%(mod/2)

# root_2 = math.sqrt(2)

# def luc(n):
# 	num_1 = ((1+root_2)**n - (1-root_2)**n) / root_2
# 	num_2 = ((1+root_2)**n + (1-root_2)**n) / 2
# 	return num_2+num_1


# n = int(raw_input())
# # print o(n+1)
lastA, lastB = luc(0), luc(1)
for i in range(0, 50):
	new = luc(i)
	print i, (lastA + lastB*2)%mod == int(round(new)), new, (lastA + lastB*2)%mod, lastA, lastB
	lastA, lastB = lastB, int(round(new))

print luc(38)
# i = 10**10
# print o(i+1), luc(i)%mod



# import numpy as math
# mod = (10**9 + 7)*2
# l1 = 1 + math.sqrt(2)
# l2 = 1 - math.sqrt(2)

# def powmod(b, e, n):
# 	x, y = 1, b; 
# 	while e > 0:
# 		if e%2 == 1:
# 			x = math.mod(math.multiply(x,y), n)
# 		y = math.mod(math.square(y), n)
# 		e = math.divide(e, 2)
# 	return x%n;

# def o(n):
# 	if n%2 == 1:
# 		n1 = math.mod(math.multiply(powmod(l1,n-1,mod), l1), mod)
# 		n2 = math.mod(math.multiply(powmod(l2,n-1,mod), l1), mod)
# 	else:
# 		n1 = powmod(l1,n,mod)
# 		n2 = powmod(l2,n,mod)
# 	# print n1, n2
# 	return int(round(math.divide(math.add(n1, n2), 2)))%(mod/2)

# n = len(raw_imathut())
# print o(n+1)