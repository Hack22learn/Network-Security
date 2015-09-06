__auther__='Sudhanshu Patel'
__email__='query.b2cs@gmail.com'

#Auto Key Cipher
def AutoKeyCipher(plainText,key):
    #Auto Key Cipher
    #only for Cpital letter
    plainText=plainText.upper()
    plainText=plainText.replace(' ','')
    cipher=[]
    #special case for 1st char
    #print key
    key=int(key)%26
    cipher.append(chr(((ord(plainText[0])-65)+key)%26 +65))
    for i in range(1,len(plainText)):
        key=ord(plainText[i-1])-ord('A')
        cipher.append(chr((((ord(plainText[i])-65)+key)%26 +65)))
    return "".join(cipher)
if __name__=="__main__":
    #plT=raw_input("plainText : ")
    plT='Attack is today'
    key=raw_input("Key (int): ")
    print AutoKeyCipher(plT,key)

# http://codecops.in
