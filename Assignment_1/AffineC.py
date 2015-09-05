try:
    from MFunctions import *
except:
    print 'Error in Importing Dependecy files'
    exit()

def AffineCipherE(st,mkey,skey):
    ''' find Affine cipher '''
    #First Validate Key has inverse
    if not findModInverse(mkey, 26):
        print "Key does't have Multiplicative inverse"
        return None
    rst=''
    
    for ch in st:
        asciiV=ord(ch)
        if asciiV>64 and asciiV<91:
            rst +=chr((((asciiV-64)*mkey)+skey)%26 +65)
        elif asciiV>96 and asciiV<123:
            rst +=chr((((asciiV-96)*mkey)+skey)%26 +97)
        else:
            rst +=ch
    return rst

if __name__=='__main__':
    print "Enter String To Encrypt using Affine Cypher"
    st=raw_input("Plain Text: ")
    key=[int(x) for x in raw_input('Enter 2 key separated by space').split(' ')]
    print  AffineCipherE(st,key[0],key[1])
    print "Thank U"
