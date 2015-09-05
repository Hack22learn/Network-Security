#__author__ = 'Sudhanshu Patel'
__author__ = 'Sudhanshu Patel'

def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b

def findModInverse(a, m):
        # finding the modular inverse just like there was for finding
        # the Greatest Common Divisor. Euclid's Extended Algorithm

    if gcd(a, m) != 1:
        return False # no mod inverse exists if a & m aren't relatively prime
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3 # // is the integer division operator
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

def Maddinverse(A,M):
    ''' Additive Inverse '''
    return (M-A)%M

if __name__=='__main__':
    print "Hi I am imported"