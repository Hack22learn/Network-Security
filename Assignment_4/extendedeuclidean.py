def extendedeuclidean(a,b):
    a0=a
    b0=b
    t0=0
    t=1
    s0=1
    s=0
    q=(a0/b0)
    r=a0-(q*b0)
    while r>0 :
        temp=t0-(q*t)
        t0=t
        t=temp
        temp=s0-(q*s)
        s0=s
        s=temp
        a0=b0
        b0=r
        q=(a0/b0)
        r=a0-(q*b0)
    r=b0
    return (r,s,t)
if __name__=="__main__":
    print "Enter a,b"
    a,b=(raw_input()).split()
    a=int(a)
    b=int(b)
    r,s,t=extendedeuclidean(a,b)
    print "gcd(",a,",",b,")=",r
    print " sa + tb = r : ",s,"*",a," + ",t,"*",b," = ",r
    if(r==1):
        while(s<0):
            s=s+b
        print a,"^(-1) mod",b," = ",s
