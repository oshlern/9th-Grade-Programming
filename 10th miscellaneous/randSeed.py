#!/usr/bin/python -u
import random,string

# flag = "FLAG:"+open("flag", "r").read()[:-1]
encflag = "BNZQ:jn0y1313td7975784y0361tp3xou1g44"
flag = ""
random.seed("random")
# for c in encflag:
# 	if c.isdigit():

for c in encflag:
	if c.islower():
		#rotate number around alphabet a random amount
		flag += chr((ord(c)-ord('a')-random.randrange(0,26))%26 + ord('a'))
		print c, "lower"
	elif c.isupper():
		flag += chr((ord(c)-ord('A')-random.randrange(0,26))%26 + ord('A'))
		print c, "upper"
	elif c.isdigit():
		flag += chr((ord(c)-ord('0')-random.randrange(0,10))%10 + ord('0'))
		print c, "digit"
	else:
		print c, "nada"
		flag += c
print flag
# for c in flag:
#   if c.islower():
#     #rotate number around alphabet a random amount
#     encflag += chr((ord(c)-ord('a')+random.randrange(0,26))%26 + ord('a'))
#   elif c.isupper():
#     encflag += chr((ord(c)-ord('A')+random.randrange(0,26))%26 + ord('A'))
#   elif c.isdigit():
#     encflag += chr((ord(c)-ord('0')+random.randrange(0,10))%10 + ord('0'))
#   else:
#     encflag += c
# print "Unguessably Randomized Flag: "+encflag