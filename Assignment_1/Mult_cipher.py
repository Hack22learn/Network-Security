#Multiplicative Inverse
__author__ = 'Sudhanshu Patel'
import sys
try:
    import MFunctions
except:
    print 'Error in Importing Dependecy files'
    
def MultCipher(st,key):
    ''' find Multiplicative Cipher '''
    #First Validate Key has inverse
    if not ModMultInverse(key, 26):
        print "Key does't have inverse"
        return None
    rst=''
    
    for ch in st:
        asciiV=ord(ch)
        if asciiV>64 and asciiV<91:
            rst +=chr(((asciiV-64)*key)%26 +64)
        elif asciiV>96 and asciiV<123:
            rst +=chr(((asciiV-96)*key)%26 +96)
        else:
            rst +=ch
    return rst
 


#print MultCipher('Sudhanshu Patel',3)
