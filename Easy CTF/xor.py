# SUMS
# nooms=open("addition.in","r")
# out=open("addition.out","w")
# sums=0
# a = nooms.read().split(",")
# for j==j in a:
#     sums+=int(j)
# out.write(str(evens)+'\n')
#
#
# EVEN STEVEN
# nooms=open("can-you-even.in","r")
# out=open("can-you-even.out","w")
# evens=0
# """
# a=['']*100
# indx=0
# for j==j in nooms.read():
#     if j==',':
#         indx+=1
#     else:
#         a[indx]+=j
# """
# a = nooms.read().split(",")
#
# for j==j in a:
#     if int(j)%2==0:
#         evens+=1
# out.write(str(evens)+'\n')

#MATH
# nooms=open("math-class.in","r")
# out=open("math-class.out","w")
# a = nooms.read().split(" ")
#
# def addition(in1,in2):
#     return str(in1+in2)
# def subtraction(in1,in2):
#     return str(abs(in1-in2))
#
# if a[0]=='add':
#     out.write(addition(int(a[1]),int(a[2]))+'\n')
# elif a[0]=='subtract':
#     out.write(subtraction(int(a[1]),int(a[2]))+'\n')

# Alpha(not)numeric
# import re
# nooms=open("looking-for-letters.in","r")
# out=open("looking-for-letters.out","w")
# a=''
# # for j in nooms.read():
# #     if not (j=='0' or j=='1' or j=='2' or j=='3' or j=='4' or j=='5' or j=='6' or j=='7' or j=='8' or j=='9'):
# #         a+=j
# a=re.sub('[^a-z\n]','',nooms.read())
# out.write(a)


# plaintext decryption
inp=open("knownplaintext1.in","r")
out=open("knownplaintext1.out","w")
out.write("HI PIZZA")

# in:  e G\x0bwU*I%N61RcZsftkboe88/uj=4B9^)Q
# out:   480c78562b4:264f373253645b7467756c636g6639392g766b3e35433:5f2:52

# in:  e dD?z\\&"J6WtTI7bm[DPyw$+kZo"E=Zn8
# out:   65453g7b5d27234b375875554:38636e5c45517:78252c6c5b6g23463e5b6f39
147
# easyctf{it's_fin4lly_over!!}
# 8$};m7r;)u!!L7:4Er|d,\\x!%2H]^xdE
# )HY[3j%@DC'&zV]Jjebk%ILxjP\\X:6qP

#change stuff
import re
import math
inp=open("string-change.in","r")
out=open("string-change.out","w")
stuff=inp.read()
stuff=stuff.split('\n')
print (stuff[0])
nums=stuff[0].split(',')
changed=stuff[1]
print (changed)
for i in nums:
    if int(i)==0:
        if changed[0]=='z':
            changed='a'+changed[1:]
        elif changed[0]=='Z':
            changed='A'+changed[1:]
        else:
            changed=chr(ord(changed[0])+1)+changed[1:]
    else:
        for j in range(int(i)-1, len(changed), int(i)):
            if j==len(changed):
                if changed[-1]=='z':
                    changed=changed[:-1]+'a'
                elif changed[-1]=='Z':
                    changed=changed[:-1]+'A'
                else:
                    changed=changed[:-1]+chr(ord(changed[-1])+1)
            else:
                if changed[j]=='z':
                    changed=changed[:j]+'a'+changed[j+1:]
                elif changed[j]=='Z':
                    changed=changed[:j]+'A'+changed[j+1:]
                else:
                    changed=changed[:j]+chr(ord(changed[j])+1)+changed[j+1:]
out.write(changed+'\n')


# #OINK
# import re
# inp=open("piglatin1.in","r")
# out=open("piglatin1.out","w")
# realinp=re.sub('[\n]','',inp.read())
# words=realinp.split(' ')
# for word in range(0,len(words)):
#     if words[word][0] in ('A','E','I','O','U','a','e','i','o','u'):
#         words[word]+='yay'
#     else:
#         words[word]+=words[word][0]
#         words[word]+='ay'
#         words[word]=words[word][1:]
# words=' '.join(words)
# out.write(words+'\n')

# #OINK OINK
# import re
# inp=open("piglatin2.in","r")
# out=open("piglatin2.out","w")
# realinp=re.sub('[\n]','',inp.read())
# words=realinp.split(' ')
# capital=0
# for word in range(0,len(words)):
#     if words[word][len(words[word])-3] == 'y':
#         words[word]=words[word][:len(words[word])-3]
#     else:
#         if re.search('[A-Z]',words[word][0]):
#             words[word]=chr(ord(words[word][0])+32)+words[word][1:]
#             capital=1
#         words[word]=words[word][len(words[word])-3]+words[word][:len(words[word])-3]
#         if capital==1:
#             words[word]=chr(ord(words[word][0])-32)+words[word][1:]
#             capital=0
# words=' '.join(words)
# out.write(words+'\n')


# #If Logic
# inp=open("if-logic.in","r")
# out=open("if-logic.out","w")
# nums=inp.read().split(',')
# for i in nums:
#     if 0<=int(i)<=50:
#         out.write('hi\n')
#     elif 51<=int(i)<=100:
#         out.write('hey\n')
#     else:
#         out.write('hello\n')


# #Sort of Easy
# import re
# inp=open("sorting-job.in","r")
# out=open("sorting-job.out","w")
# nums=p=re.sub('[\n]','',inp.read())
# nums=nums.split(',')
# order=[]
# for i in nums:
#     if i==nums[0]:
#         order=[i]
#     else:
#         x=0
#         for j in range(0,len(order)):
#             if x==0:
#                 if (int(i)>int(order[j] or int(i)==int(order[j])):
#                     if j==0:
#                         order=[i]+order
#                     else:
#                         order=order[:j]+[i]+order[j:]
#                     x=1
#
#         if x==0:
#             order=order+[i]
# order=','.join(order)
# out.write(order+'\n')
