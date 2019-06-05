def generate(array):
    zeros = [i for i, x in enumerate(array) if x == 0]
    if len(zeros) != 0:
        new = [0] * len(array)
        if len(zeros) > 1:
            return new
        else:
            product = 1
            for i in range(zeros[0]) + range(zeros[0] + 1, len(array)):
                product *= array[i]
            new[zeros[0]] = product
            return new
    else:
        new = []
        product = 1
        for num in array:
            product *= num
        for num in array:
            new += [product/num]
        return new
print generate([1, 2, 3, 123, 24, 12])


#calculate a_j-1 * a_j and a_j * a_j+1 for each j
