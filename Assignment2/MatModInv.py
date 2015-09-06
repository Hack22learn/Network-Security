import numpy as np

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


def matrixModInv(mt):
    # return Matrix moduler Inverse
    domain=26 # for english character
    mt=np.array(mt)
    #calculate adjoint
    detM=int(round(np.linalg.det(mt)))
    print detM
    adj=np.linalg.inv(mt)*detM

    #data in adjoint are float convert them to int
    for i in range(len(adj)):
        for j in range(len(adj[i])):
            adj[i][j]=int(round(adj[i][j]))
    # Find Moduler Inverse of
    detI=findModInverse(abs(int(detM)), domain)
    print "Moduler Inverse of det(M):",detI
    if detI:
            if detM >=0:
                modI= adj*detI
            else:
                modI=-1*adj*detI
    else:
        print "Moduler inverse does't exits"
        return False

    #Taking additive moduler Inverse of all
    for i in range(len(modI)):
        for j in range(len(modI[i])):
            modI[i][j]=int(modI[i][j]%domain)
    return np.array(modI)

if __name__=='__main__':
    mt=[[9,7,11,13],[4,7,5,6],[2,21,14,9],[3,23,21,8]]
    print matrixModInv(mt)
