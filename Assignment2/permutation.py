__auther__='Sudhanshu patel@Tm'
__email__='query.b2cs@gmail.com'

#permutation Cipher
#Also Known As Keyd Transposition Cipher

import numpy as np
import collections
import string
def EpermutationCipher(pMat,plainText , encryption=True):
    #return cipherText
    #return plain text

    if encryption:
        #basic plainText Preprocessing
        plainText=plainText.upper()
        for punc in string.punctuation:
            plainText=plainText.replace(punc,'')
        plainText=plainText.replace(' ','')
        print 'PlainText after preProcessing :',plainText
        
    def permutationEmatrix(pStream):
        #pStream -permutation stream
        #return permuation matrix
        
        keyMat=[]
        for i in range(len(pStream)):
            keyMat.append([int(0) for x in range(len(pStream))])
            
        for col in range(len(pStream)):
            keyMat[pStream[col]-1][col]=1
        return keyMat

    def plainTextMat(pText,l):
        # l->len(pStream)
        #return plainText Matrix
        
        ptMat=[] #plainText Mat
        lp,ind,i=len(pText),0,0

        while True:
            if ind>=lp: break
            else:       ptMat.append([])
            for j in range(l):
                if ind<lp:
                    ptMat[i].append(ord(pText[ind])-ord('A'))
                    ind +=1
                else: ptMat[i].append(ord('Z')-ord('A'))
            i+=1
        return ptMat
    def decryptStream(pMat):
        #return decrypt permutation
        d = collections.defaultdict( int )
        for i in range(len(pMat[0])):
            d[pMat[0][i]]=pMat[1][i]
        permutation=[]
        for i in range(1,len(d)+1):
            permutation.append(d[i])
        return permutation
    
    #Chossing permutation Key based on Encription or decription process
    if encryption: pStream=pMat[0]
    else: pStream=decryptStream(pMat)
    
    l=len(pStream)
    #converting permutation in marix formate
    keyMat=permutationEmatrix(pStream)
    print "key Mat:\n", np.array(keyMat) #debugg

    #converiting PlainText In matrix formate
    ptMat=plainTextMat(plainText,l)
    print "textMat :\n",np.array(ptMat)

    # Apply Cross product to get Encrypted msg in matrix form
    cipherMat=np.dot(ptMat,keyMat)
    print "Cipher Matrix : textMatrix* keyMatrix\n",np.array(cipherMat)
    
    # convert Cipher Matrix in text, in row_major Approch
    cipher=[]
    for i in range(len(cipherMat)):
        for j in range(len(cipherMat[i])):
            cipher.append(cipherMat[i][j])
    
    return "".join([chr(ch+ord('A')) for ch in cipher])
    
                          
    

if __name__=='__main__':
    # initialise Permutation Matrix
    #pMat=[[1,2,3,4,5,6,7,8],[4,1,6,2,7,3,8,5]]
    #plainText="TGEEMNELNNTDROEOAAHDOETCSHAEIRLM"

    pMat=[[3,1,4,5,2],[1,2,3,4,5]]
    plainText="enemyattackstonightz"
    
    
    # Encyption
    print "\n\n Encrypting .\n.................."
    Encrypt=EpermutationCipher(pMat,plainText)
    print "\n\n\n"
    print "Encrypted Text =",Encrypt
    
    print "\n\nNow Decrypting .\n.................."
    # Decryption
    decrypt=EpermutationCipher(pMat,Encrypt,False)
    print "\n\nDecrypted Text :",decrypt
                         
                         
