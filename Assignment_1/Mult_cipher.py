#Multiplicative Inverse
__author__ = 'Sudhanshu Patel'
import sys
try:
    from MFunctions import *
except:
    print 'Error in Importing Dependecy files'
    
def MultCipher(st,key):
    ''' find Multiplicative Cipher '''
    #First Validate Key has inverse
    if not findModInverse(key, 26):
        print "Key does't have inverse"
        return None
    rst=''
    
    for ch in st:
        asciiV=ord(ch)
        if asciiV>64 and asciiV<91:
            rst +=chr(((asciiV-65)*key)%26 +65)
        elif asciiV>96 and asciiV<123:
            rst +=chr(((asciiV-97)*key)%26 +97)
        else:
            rst +=ch
    return rst
 


if __name__=='__main__':
    print "Enter String To Encrypt using Affine Cypher"
    st=raw_input("Plain Text: ")
    key=int(raw_input('Enter key:'))
    print  MultCipher(st,key)
    print "Thank U"
