def AffineCipherE(st,mkey,skey):
    ''' find Affine cipher '''
    #First Validate Key has inverse
    if not ModMultInverse(mkey, 26):
        print "Key does't have inverse"
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
