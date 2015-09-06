__auther__='Sudhanshu patel@Tm'
__email__='query.b2cs@gmail.com'

#importing matrix Moduler Inverse function from MatModInv.py
from MatModInv import *
import numpy as np

def plainTextMat(pText,l):
        # l->len(keyMat) i.e Block Size
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
		#if no of char remaining is less than block size
		#remainig place is filled with 0 
                else: ptMat[i].append(0)
            i+=1
        return np.array(ptMat)
def Mat2Text(cipherMat):
	#convert Matrix data in text stream
	# convert Cipher Matrix in text, in row_major Approch
    	cipher=[]
    	for i in range(len(cipherMat)):
        	for j in range(len(cipherMat[i])):
            		cipher.append(int(cipherMat[i][j])%26)
    			#taking Modulo with 26 {domain of plaintext}
    	return "".join([chr(ch+ord('A')) for ch in cipher])

def Hill_Cipher(plainText,keyMat,decryption=False):
	plainText=plainText.upper()
	#Use to Encrypt and decrypt by Hill Cipher
	# if decrypt==False it encyipt Else decrypt

	if decryption: keyMat=matrixModInv(keyMat)
	try:	
		if len(keyMat) <=0: return False
	except:
		return False
	#convert plainText in Matrix Formate
	ptM=plainTextMat(plainText,len(keyMat))

	#CipherMatrix =plainTextMat cross Product KeyMat
	cipherMat=np.dot(ptM,keyMat)

	#Taking Modulo With 26 i.e doaminSize
	cipherMat=Matmodulo(cipherMat,domain=26)
	print """Cipher/Plaintext Matrix \n\n""",cipherMat
	
	#convert to textual formate
	return Mat2Text(cipherMat)
	
	 

if __name__=='__main__':
	keyMat=mt=[[9,7,11,13],[4,7,5,6],[2,21,14,9],[3,23,21,8]]
	# Number of row in ley matrix must be equal to no of column
	# in plainText Matrix, that is block size of plainText Matrix
	plainText="OnceMoreIntoTheFrayIntoLastGoodFightIwillEverKnow"
	
	print "\n\nEncryption .........."
	Cipher=Hill_Cipher(plainText,keyMat)
	print '\nCipher Text :\n',Cipher

	print "\n\nDecryption .........."
	Decryptedtext=Hill_Cipher(Cipher,keyMat,True)
	if Decryptedtext !=False:
		print "\nDecrypted text :\n",Decryptedtext
	else:
		print "DEcryption Not Possible"
