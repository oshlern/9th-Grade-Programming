import math
def add(v1,v2):
    sum = 0
    for num in v1:
        var = num*v1

    print small
    print big
    for digit1 in range(len(small)):
        for digit2 in range(len(big)):
            if len(new)<=(digit1*digit2):
                new += [small[digit1]*big[digit2]]
            else:
                new[digit1*digit2] += small[digit1]*big[digit2]
            # print digit1*digit2
            # print 'x'
            # print small[digit1]*big[digit2]
            # print 'y'
# def product(list1,list2):

def phi(n):
    product = [1]
    for i in range(1,n):
        product *= (1-math.pow(10,i))
    return product

# for i in range(20):
    # print phi(i)
print add([1,2,3,4,5],[1,1,1])
