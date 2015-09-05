__author__ = 'Sudhanshu Patel'

def playfair(st,mat):
    '''
      Playfair Cipher Encryption
      Space, Numbers & punctuation Is not allowed
    '''
    #string Process Add bouge characer "X"
    i=1
    while(i<len(st)):
        if st[i]==st[i-1]:
            st=st[:i]+'X'+st[i:] #add 'X' in between if conscutive char are same
        i+=1

    if(len(st)%2!=0): #if lengh is odd then add bouge letter
        st+='X'

    # to make searching faster use save index of each

    dct=dict()
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] not in dct:
                dct[mat[i][j]]=[i,j]
                if mat[i][j]=='I':
                    dct['J']=[i,j]
    print st
    rst=""
    # Encriptyning
    col=len(mat)
    row=len(mat[0])
    i=0
    while(i<len(st)):
        #case 1 both are in same row
        if dct[st[i]][0]==dct[st[i+1]][0]:
            r=dct[st[i]][0]
            rst +=mat[r][(dct[st[i]][1]+1)%row]+mat[r][(dct[st[i+1]][1]+1)%row]
        #case 2 both are in same col
        elif dct[st[i]][1]==dct[st[i+1]][1]:
            c=dct[st[i]][1]
            rst +=mat[(dct[st[i]][0]+1)%row][c]+mat[(dct[st[i+1]][0]+1)%row][c]
        #case 3 not in same row or col
        else:
            rst+=mat[dct[st[i]][0]][dct[st[i+1]][1]] + mat[dct[st[i+1]][0]][dct[st[i]][1]]
        i+=2
    return rst



if __name__=='__main__':
    EncripM=[['L','G','D','B','A'],['Q','M','H','E','C'],['U','R','N','I','F'],['X','V','S','O','K'],['Z','Y','W','T','P']]
    st=raw_input('Input>>')

    print(playfair(st.upper(),EncripM))
