import math
num='3845281945283805284526053525260547380516453748164748478317454508'
    #  e  a  s  y  a  s  e  O  s  a  X  O           O  Z  e  O  Y  a     W  Y  Z  W  Z        a  a
    #  A  e  B  y  e  B  A  O  B  e  X  O           O  Z  A  O  Y  e     W  Y  Z  W  Z  s  l  e  e  p

nums=[]
out=''
letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(0,len(num),2):
    nums+=[int(num[i:i+2])]
for i in nums:
    out+=letters[i%26]
print out
