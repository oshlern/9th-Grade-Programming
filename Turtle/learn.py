import turtle

turtle.shape("turtle")
turtle.speed("fastest")

turtle.forward(10)
turtle.right(100)

# b1 = [10, 3]
# b2 = [5, 10]
# b3 = [15, 7]
# bananas = [b1, b2, b3, 4]
# for b in bananas:


def find(n):
    if n==2:
        return 2
    if n==1:
        return 1
    return find(n-1) + find(n-2)
print find(5)
# fib = [1,2]
# for i in range(1, 1000001):
#     new = fib[-1] + fib[-2]
#     fib += [new]
# while True:
#     new = fib[-1] + fib[-2]
#     fib += [new]
#     print new

# print fib

# s = 1
# for i in range(1, 10001):
#     s = s * i
# print s
