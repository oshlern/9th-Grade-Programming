def pent(r):
    if r==0:
        return 1
    var = pent(r-1)+3*r+1
    # print var
    return var

print pent(500)
