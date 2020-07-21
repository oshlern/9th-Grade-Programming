from operator import mul, mod
import math
import numpy as np
# https://gist.github.com/sirodoht/ee2abe82eca70f5b1869
def numToAscii(m, nchars):
    print ''.join(chr((m>>8*(nchars-byte-1))&0xFF) for byte in range(nchars))
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)

def modInv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        print a, m
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def crt(a, m): # tuples 3 long
    # x =  (sum(rem[i]*pp[i]*inv[i]) ) % prod
    M = reduce(mul, m) # the product of m elements
    m_i = [np.divide(M, item) for item in m] # = m but reverse
    # print m_i, m
    b = map(modInv, m_i, m)
    e = map(mul, m_i, b)

    x_sum = sum(map(mul, a, e))
    x = x_sum % M
    return x



# https://wizardry-and-studies.blogspot.com/2005/11/chinese-remainder-theorem-in-python.html
# conditions = { a1 : n1, a2 : n2 ... }
# def crt(conditions):
#     product = reduce(lambda x,y: x*y, conditions.values())
#     print range(1,4,2)
#     sequences = [ set(range(a, product, n)) for a, n in conditions.iteritems() ]
#     result = list(reduce(lambda x,y: x & y, sequences))
#     return result

# http://eli.thegreenplace.net/2009/03/07/computing-modular-square-roots-in-python
def modular_sqrt(a, p):
    """ Find a quadratic residue (mod p) of 'a'. p
        must be an odd prime.

        Solve the congruence of the form:
            x^2 = a (mod p)
        And returns x. Note that p - x is also a root.

        0 is returned is no square root exists for
        these a and p.

        The Tonelli-Shanks algorithm is used (except
        for some simple cases in which the solution
        is known from an identity). This algorithm
        runs in polynomial time (unless the
        generalized Riemann hypothesis is false).
    """
    # Simple cases
    #
    if legendre_symbol(a, p) != 1:
        print "RIP"
        return 0
    elif a == 0:
        return 0
    elif p == 2:
        return a
    elif p % 4 == 3:
        return pow(a, (p + 1) / 4, p)

    # Partition p-1 to s * 2^e for an odd s (i.e.
    # reduce all the powers of 2 from p-1)
    #
    s = p - 1
    e = 0
    while s % 2 == 0:
        s /= 2
        e += 1

    # Find some 'n' with a legendre symbol n|p = -1.
    # Shouldn't take long.
    #
    n = 2
    while legendre_symbol(n, p) != -1:
        n += 1

    # Here be dragons!
    # Read the paper "Square roots from 1; 24, 51,
    # 10 to Dan Shanks" by Ezra Brown for more
    # information
    #

    # x is a guess of the square root that gets better
    # with each iteration.
    # b is the "fudge factor" - by how much we're off
    # with the guess. The invariant x^2 = ab (mod p)
    # is maintained throughout the loop.
    # g is used for successive powers of n to update
    # both a and b
    # r is the exponent - decreases with each update
    #
    x = pow(a, (s + 1) / 2, p)
    b = pow(a, s, p)
    g = pow(n, s, p)
    r = e

    while True:
        t = b
        m = 0
        for m in xrange(r):
            if t == 1:
                break
            t = pow(t, 2, p)

        if m == 0:
            return x

        gs = pow(g, 2 ** (r - m - 1), p)
        g = (gs * gs) % p
        x = (x * gs) % p
        b = (b * g) % p
        r = m


def legendre_symbol(a, p):
    """ Compute the Legendre symbol a|p using
        Euler's criterion. p is a prime, a is
        relatively prime to p (if p divides
        a, then a|p = 0)

        Returns 1 if a has a square root modulo
        p, -1 otherwise.
    """
    ls = pow(a, (p - 1) / 2, p)
    return -1 if ls == p - 1 else ls




p= 13013195056445077675245767987987229724588379930923318266833492046660374216223334270611792324721132438307229159984813414250922197169316235737830919431103659
q= 12930920340230371085700418586571062330546634389230084495106445639925420450591673769061692508272948388121114376587634872733055494744188467315949429674451947

e= 100

CC= 2536072596735405513004321180336671392201446145691544525658443473848104743281278364580324721238865873217702884067306856569406059869172045956521348858084998514527555980415205217073019437355422966248344183944699168548887273804385919216488597207667402462509907219285121314528666853710860436030055903562805252516

# e isn't coprime, gcd(e, lam) = 2
# D + 1/e (real 1/e? there is no inverse)
lam = 84136294323385483438649994124974693353865320388360264700465956188343934636944408638507451238954464709433591838764407839288237734970825038493294620488643756765016000966811684948309440760973569390322399594194164755294352213590435561770349469894496835532577115034837769530080997134347370344650507094178532909234
# print lam % 5, "ASD"
# print pow(e, (lam-1)/2, lam) % 8

# p = 7
# q = 11
# C = 36*36*36*36%(p*q)
# C = CC
# pc = modular_sqrt(CC%p, p)
# qc = modular_sqrt(CC%q, q)
# Ca = int(crt((pc, qc), (p, q)))
# pc = modular_sqrt(Ca%p, p)
# qc = modular_sqrt(Ca%q, q)
# c = int(crt((pc, qc), (p, q)))
# n = np.multiply(p,q)
# d = modInv(e/4, lam)
# m = pow(c, d, n)
# # print "MESSAGE:  ", m
# # print pow(m, e, n) == CC
# numToAscii(m, 1000)

# pc = modular_sqrt(CC%p, p)
# qc = modular_sqrt(CC%q, q)
# conditions1 = ((pc, qc), (p, q))
# conditions2 = ((p-pc, qc), (p, q))
# conditions3 = ((pc, q-qc), (p, q))
# conditions4 = ((p-pc, q-qc), (p, q))
# C1 = int(crt(conditions1[0], conditions1[1]))
# C2 = int(crt(conditions2[0], conditions2[1]))
# C3 = int(crt(conditions3[0], conditions3[1]))
# C4 = int(crt(conditions4[0], conditions4[1]))
# Cs = [C1, C2, C3, C4]
# for C in Cs:
#     pc = modular_sqrt(C%p, p)
#     qc = modular_sqrt(C%q, q)
#     conditions1 = ((pc, qc), (p, q))
#     conditions2 = ((p-pc, qc), (p, q))
#     conditions3 = ((pc, q-qc), (p, q))
#     conditions4 = ((p-pc, q-qc), (p, q))
#     c1 = int(crt(conditions1[0], conditions1[1]))
#     c2 = int(crt(conditions2[0], conditions2[1]))
#     c3 = int(crt(conditions3[0], conditions3[1]))
#     c4 = int(crt(conditions4[0], conditions4[1]))
#     cs = [c1, c2, c3, c4]
#     for c in cs:
#         n = np.multiply(p,q)
#         d = modInv(e/4, lam)
#         m = pow(c, d, n)
        # print pow(m, e, n) == CC
        # numToAscii(m, 1000)
# C = int(crt((pc, qc), (p, q)))
# print C

# n = np.multiply(p,q)

# d = modInv(e/4, lam)
# m = pow(C, d, n)
# print "MESSAGE:  ", m
# print pow(m, e, n) == CC

# 111111100110111011010100010010000000011001101011100101011010010101011011010000101010011110011111010101101101100001001001101000011100101000000011010100100000111011101011100110000011000010011000110001010010011110010011111100110010001000000001001001011001111000001101100111100000010010011101100110011110001011010000110111101010001101010100110101010000110000011010101101000001101011000000111100100100100111000100100101011110000111100100110110001100011010111101101000111100011111010011100000101000110100101100111111100111011010101100010001000001001111010010110101011100000100001000100101110111110000010011000101100100000110010101101110100101011110011011001101100111111111000111011010101101110101101011111001110100111011100010101001011001000010011100000100100001101010011010111100010101010100100000000101100111110011111000100001011100111101101101111001110101101001000100011100101100111111001010101111100001101100010000000001100000001001000001110001111001101000101010110110100001000101100111000001100001111110100110100101100101000
# print numToAscii(m, 100)
# # C = 64%(p*q)
# print C, C%p, C%q
# pc = modular_sqrt(C%p, p)
# qc = modular_sqrt(C%q, q)
# print pc,qc
# # print p-pc
# # print p
# # print qc
# # print q-qc
# # print q 
# # conditions = {pc: p, p-pc: p, qc: q, q-qc: q}
# conditions1 = ((pc, qc), (p, q))
# conditions2 = ((p-pc, qc), (p, q))
# conditions3 = ((pc, q-qc), (p, q))
# conditions4 = ((p-pc, q-qc), (p, q))

# # 7*11 = 77
# # print crt((431%7, 431%11, 431%13), (7, 11, 13)), "ASD"
# C1 = crt(conditions1[0], conditions1[1])
# C2 = crt(conditions2[0], conditions2[1])
# C3 = crt(conditions3[0], conditions3[1])
# C4 = crt(conditions4[0], conditions4[1])
# Cs = [C1, C2, C3, C4]
# print C1, "ASDHIGUYF", C1%(p*q)
# print C1 == 64%(p*q)
# c = 64%(p*q)
# pc = modular_sqrt(c%p, p)
# qc = modular_sqrt(c%q, q)
# print pc, qc, "ASL:DKJ"
# for c in Cs:
#     print c, c%p, c%q
#     if c == 64%(p*q):
#         c = 64%(p*q)
#     pc = modular_sqrt(c%p, p)
#     qc = modular_sqrt(c%q, q)
#     print pc, qc
#     if pc != 0 and qc != 0:
#         C = c
#         print pc, qc, C
#         break
#         # Maybe more
# print pc, qc
# print C, C%p, C%q

# # C = 64%(p*q)
# # pc = modular_sqrt(C%p, p)
# # qc = modular_sqrt(C%q, q)
# # print pc, qc
# conditions1 = ((pc, qc), (p, q))
# conditions2 = ((p-pc, qc), (p, q))
# conditions3 = ((pc, q-qc), (p, q))
# conditions4 = ((p-pc, q-qc), (p, q))
# C1 = crt(conditions1[0], conditions1[1])
# C2 = crt(conditions2[0], conditions2[1])
# C3 = crt(conditions3[0], conditions3[1])
# C4 = crt(conditions4[0], conditions4[1])
# Cs = [C1, C2, C3, C4]
# print Cs


# Find sqrt(C) mod n by finding sqrt(C) mod p,q and using chinese remainder theorem
# c = sqrt(sqrt(C)) actually
# Find d for e=25 (e^-1 mod lam)
# take c^d mod n
# d = np.true_divide(lam + 1, e)
# d, remainder = int(math.floor(d)), d - math.floor(d)
# m = pow(c, d, n)
# print m
print "Done"
# print numToAscii(m, 10000)
# print modInv(e, lam)





# RSA 3

n = 0x27335d21ca51432fa000ddf9e81f630314a0ef2e35d81a839584c5a7356b94934630ebfc2ef9c55b111e8c373f2db66ca3be0c0818b1d4eda7d53c1bd0067f66a12897099b5e322d85a8da45b72b828813af23L
e = 0x10001
c = 0x9b9c138e0d473b6e6cf44acfa3becb358b91d0ba9bfb37bf11effcebf9e0fe4a86439e8217819c273ea5c1c5acfd70147533aa550aa70f2e07cc98be1a1b0ea36c0738d1c994c50b1bd633e3873fc0cb377e7L
# k*n + c   ^ 1/e = m
ne = np.true_divide(1, e)
# # print ne
# for i in range(100000):
#     if np.power(np.add(np.multiply(n, i), c), ne).is_integer():
#         print i
#         break
# print "S"








# n = 0xafaab4675d563b655bb03ed0a083ea91e8309ea884f453a6e9204a40cb61f6c6d28546fc9099c09238fbe6ea7f6646662e26ddd9cfb9d1d57187f5747dabe82b5d622d73ed2b2fd45de289aa047cf2a750bf899a42ac7b9a600d81d91680fd102dcaef933f5e163abb3f9397e5630153ceb1df3f91f1a9567f70e10bbbd47febac0cebe52a48192c3bf41ceef91ea41283dd4b9c4bc923f9c859634382dfca21f31de0b788542177e7f882bb960f0de6e72f25ff75cc6ba082a1ca3c21203a836e308c656c31c55ba71983da16e134642ff64caa1d3a4976c7c1bc81aa1fc4ca04741355a8128c11ae1a1b1920d581ddeee58f327e4cc5a33fbe6551ebde204108b4cf51b72dd823ff5af15ffa0002da249fb3379ea389dfaea139bb8f1abc42d8847980f2f0909906e3fad65f3e0cd8c40a84ea0babec01d65b2506fe15e905df8217909df663e4f403099fb2a37797abda09ebd89681f5fc8890b542689bd0f81d435926cb3679d64091eb2fb65311bac2e7713eb195837a3fe3d60c31b7f1d98823f1adc6946c0a19febade9a614c3008893fb63e32772336c7572a6058fa0303c26ba91a71bc617447e8f26dcbc200ca50165c4bfc531b83e0e39f03b68068b551fc6de19e4324e877b0474724bc221e9ff1a021305fecaaafbca01d165d1428ccd2523a5ae44ad38ce28ca97df8c3e2ca606513dc06939d5211a02a882bL
# e = 0x10001
# d = 0x1582702b8a38e531cdf0a21f10d53dba5f067edd8a0307a1c5ceddea49ccec4a50d07e9d51be4e185f5e71ff5a866d2a4a1b0dd0da39d5b85ff5cc7f3373681dee5579610ea6e9b9855f8dc4cc8607fc7855333f1dbc3cd81480dc61a440a5381c55d98e4ea2a90e7d8fbd9431f3325ae9e255c27493c53c4cfa0d7de7ac3cf0134805897a348a3788b4a792cd3650e9113b77077af3969fb7bb70159771ca9f1ed92f6e2a0c1fa3d4715d2086cf5ca1ade9fedcb7ee756981320bf578ae714289766b62e58c90aa3b4531d703099112857200f3e7e6baadda1adec4564edbf044e2698a5d032b6633f0cdece13ff5b9ef4b625f037abc72e03741711646ee651L
# c = 0x9e44c7eff98f01845ed2c2ce6542f7b3a545785ee48d70848bd9a0760fc6343e655983401c80ae5318c428c4b4b093f6dca6505b6f6d63c707ea3a9db683a8bfd083d291995a516dbe12adc6cd7eba1d6121fbb98d5990c2d058e35ff07ea19bd1cb627cab7ead543496e8111bad4b608889f9bc625a42f4e613c8d88538f09ee1126b8fb7f4954b6a9acb268ad5a47be6cd0493494acb2168e002b98b6dc49d2ec25b7b104bc6bfdc2bf748ff8d97b20b2a6c43b8d772c13f0c58d1822a72e6c9cb5fd64a260cf61d1bd2c05cce612bd55e551c202c706b3b0ce3bf973bd4ff160e381fac81d3236d0f555c9cd25682ce1df726c0902c707aa43cf66f9f5d55d6099be160d4ebb300fa786c8e3b537e6bd2c0caba71aa2c5a73d09e5ddb9eeab70c3a622337dac39544ead7a0af4b1c39cc46fcc68316db678f936ee483c2aa69359c88c27dd4d87393cb2821d11e59065df847ded49e7ae1171e2bd2b10dc5d77d407f9f701b1175cb3f57bdd5824c6a98b944fa59770598a1658c02a05c46c7bf172e014d6ed0f852bae56654f189efe5e724c1f99d612e7b8b0666d099c6011b6722998043f025771dd842598ef12a64ecf0a812ddd011740fd1a60ae6fdbce98c988a93d4b50213fccbe5f4d866a3d09806ac6ba9806f2784badf19e6084b4e00ef77e02c70be91a9773a8bf6bb7fa68cdc32a616a28365baef8a26a3d2L
# print math.log(e)/math.log(n)
# bd = bin(n)
# print n%4 # 3
# print len(bd) #2049 least sig bits d #4096 (2^12) n
# bd, 101011000001001110000001010111000101000111000111001010011000111001101111100001010001000011111000100001101010100111101101110100101111100000110011111101101110110001010000000110000011110100001110001011100111011011101111010100100100111001100111011000100101001010000110100000111111010011101010100011011111001001110000110000101111101011110011100011111111101011010100001100110110100101010010010100001101100001101110100001101101000111001110101011011100001011111111101011100110001111111001100110111001101101000000111011110111001010101011110010110000100001110101001101110100110111001100001010101111110001101110001001100110010000110000001111111110001111000010101010011001100111111000111011011110000111100110110000001010010000000110111000110000110100100010000001010010100111000000111000101010111011001100011100100111010100010101010010000111001111101100011111011110110010100001100011111001100110010010110101110100111100010010101011100001001110100100100111100010100111100010011001111101000001101011111011110011110101100001111001111000000010011010010000000010110001001011110100011010010001010001101111000100010110100101001111001001011001101001101100101000011101001000100010011101101110111000001110111101011110011100101101001111110110111101110110111000000010101100101110111000111001010100111110001111011011001001011110110111000101010000011000001111110100011110101000111000101011101001000001000011011001111010111001010000110101101111010011111111011011100101101111110111001110101011010011000000100110010000010111111010101111000101011100111000101000010100010010111011001101011011000101110010110001100100100001010101000111011010001010011000111010111000000110000100110010001000100101000010101110010000000001111001111100111111001101011101010101101110110100001101011011110110001000101011001001110110110111111000001000100111000100110100110001010010111010000001100101011011001100011001111110000110011011110110011100001001111111111010110111001111011110100101101100010010111110000001101111010101111000111001011100000001101110100000101110001000101100100011011101110011001010001




c = 95272795986475189505518980251137003509292621140166383887854853863720692420204142448424074834657149326853553097626486371206617513769930277580823116437975487148956107509247564965652417450550680181691869432067892028368985007229633943149091684419834136214793476910417359537696632874045272326665036717324623992885
p = 11387480584909854985125335848240384226653929942757756384489381242206157197986555243995335158328781970310603060671486688856263776452654268043936036556215243
q = 12972222875218086547425818961477257915105515705982283726851833508079600460542479267972050216838604649742870515200462359007315431848784163790312424462439629
dp = 8191957726161111880866028229950166742224147653136894248088678244548815086744810656765529876284622829884409590596114090872889522887052772791407131880103961
dq = 3570695757580148093370242608506191464756425954703930236924583065811730548932270595568088372441809535917032142349986828862994856575730078580414026791444659
# n = p*q
# qInv = modInv(q,p)
# m1 = pow(c,dp,p)
# m2 = pow(c,dq,q)
# h = qInv*(m1-m2) % p
# m = m2 + h*q
# print numToAscii(m,1000)
c = 150815
d = 1941
n = 435979
print pow(c,d,n)

