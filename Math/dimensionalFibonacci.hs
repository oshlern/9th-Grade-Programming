# make functions to print fibonacci to find any f(n) = sum(i=1 to k)(f(n-i))
latestFib n j k sum = if (k == 0) sum else latestFib n j k-1 (+ sum fib n-k j)
fib n j = if (n <= j) 1 else return latestFib n j j
