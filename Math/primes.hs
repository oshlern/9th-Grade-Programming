primesList = [11,13,17,19,23,27,] everything that is not a multiple of [2,3,5,7] up until 2*3*5*7=n
return n list
isPrime 1 = False
isPrime 2 = True
// figure out base cases with primeList and such
isPrime x = isPrimeHelper x n primesList(log(n))

isPrimeHelper x n nj list =
for i in list
  if (mod x (nj+i) == 0)
    return false
  else
    return isPrimeHelper x n (nj+n) list
maybe add n to all of list every time

list x nj len = 
