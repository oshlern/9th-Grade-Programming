def g(x):
    if x==0:
        return 0
    if x==1:
        return 1
    return (g(x-1)+g(x-2))**2

def w(x):
    if x==0:
        return 0
    if x==1:
        return 1
    return (w(x-1)**2)+(w(x-2)**2)

def f(x):
    return g(x)-w(x)

def sumf(x):
    a=str(abs(f(x)))
    sums=0
    for i in a:
        sums+=int(i)
    return sums


print sumf(13)
# print sumf(24)
