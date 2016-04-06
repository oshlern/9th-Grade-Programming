import random, math
nums=[]
# [1,6,2,10,3,8,9,3,5,60,1,48,72,75,28,94,27,48]
for i in xrange(200):
    nums+=[random.randint(0,1000)]

def smallest(array):
    newArray=[]
    l=len(array)
    while len(array)>0:
        smallest=0
        for i in range(len(array)):
            if array[smallest]>array[i]:
                smallest=i
        newArray+=[array.pop(smallest)]
    return newArray
def merge(array):
    if len(array)==1:
        return array
    else:
        array1=array[:math.floor(len(array)/2)]
        array2=array[math.floor(len(array)/2):]
print smallest(nums)
