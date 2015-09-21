__auther__='Sudhanshu Patel'
__email__='query.b2cs@gmail.com'

#Vigenere Cipher
    
def VigenereCipher(plainText,keys):
    # Vigenere Cipher
    plainText=plainText.upper()
    plainText=plainText.replace(' ','')
    block=len(keys)
    sizep=len(plainText)
    cipher=[]
    for i in range(0,sizep,block):
        if i+block<=sizep:
            for j in range(i,i+block):
                cipher.append(chr((((ord(plainText[j])-64)+keys[j-i])%26 +64)))
        else:
            for j in range(i,sizep):
                cipher.append(chr((((ord(plainText[j])-64)+keys[j-i])%26 +64)))
    return "".join(cipher)
if __name__=='__main__':
    pt=raw_input("Plain Text : ")
    key=[int(x) for x in raw_input("key Stream : ").split(' ')]
    print "Vigenere Cipher"
    print VigenereCipher(pt,key)

# http://codecops.in
