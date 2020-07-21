import numpy as np

expecteds = []
numNs = 10
for n in range(1, numNs + 1):
    length = 2*n
    total = 0
    for i in xrange(100000):
        matrix = np.random.choice([0, 1], size=(length,length))
        # print np.subtract(matrix, np.transpose(matrix))
        total += np.linalg.det(np.subtract(matrix, np.transpose(matrix)))
        # print total
    total /= 100000
    expecteds.append(total)
    print n, total

for i in range(1, numNs):
    print expecteds[i]/expecteds[i-1]
