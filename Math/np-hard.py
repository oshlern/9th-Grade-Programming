import random
import math
# A Dynamic Programming based Python Program for 0-1 Knapsack problem
# Returns the maximum value that can be put in a knapsack of capacity W
def knapSack(W, wt, val, n):
    K = [[0 for x in range(W+1)] for x in range(n+1)]

    # Build table K[][] in bottom up manner
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    return K[n][W]

# Driver program to test above function
val = [60, 300, 100, 120, 150, 200]
wt = [10, 200, 20, 30, 39, 100,]
for i in range(10):
    val+=[int(math.floor(random.randint(100,10000)*math.sqrt(i)))]
    wt+=[int(math.floor(random.randint(100,10000)*math.sqrt(i)))]


W = int(random.randint(1000,1000000))
n = len(val)
print(knapSack(W, wt, val, n))


# BAD BELOW
# find out ratios
# fill best ratio until can't
# fill next best ratio until can't
# repeat until full or out of items

# N divisions for values weight ratio
# sort ratios
# N (division,flooring,multiplication,subtraction) (find the amount of each item to fill - division and floor, then subtract item weight*number of items from weight)
#   or (division w/ remainder)
