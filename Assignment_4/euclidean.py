def euclidean(a,b):
    q=[]
    if(a<b):
        t=b
        b=a
        a=t
    r0=a
    r1=b
    m=1
    while(r1!=0):
        q.append(r0/r1)
        r2=(r0-(q[m-1]*r1))
        r0=r1
        r1=r2
        m=m+1
    return (q,r0)
if __name__=="__main__":
    print "Enter a,b"
    a,b=(raw_input()).split()
    a=int(a)
    b=int(b)
    q,r=euclidean(a,b)
    print "Quotients ",q
    print "gcd(",a,",",b,")=",r
    
    
