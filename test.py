a = 0

print(a)

def f():
    global a
    a += 1

f()

print(a)
