def modinverse(a,b):
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
    return s
def crt(a1,n1,a2,n2,a3,n3):
    m1=n2*n3
    m2=n1*n3
    m3=n1*n2
    ans=a1*m1*modinverse(m1,n1)+ a2*m2*modinverse(m2,n2)+a3*m3*modinverse(m3,n3)
    N=n1*n2*n3
    while(ans>N):
        ans=ans-N
    while(ans<0):
        ans=ans+N
    return (ans,N)
if __name__=="__main__":
    print "Enter a1,a2,a3 "
    a1,a2,a3=(raw_input()).split()
    a1=int(a1)
    a2=int(a2)
    a3=int(a3)
    print "Enter n1,n2,n3 "
    n1,n2,n3=(raw_input()).split()
    n1=int(n1)
    n2=int(n2)
    n3=int(n3)
    x,N=crt(a1,n1,a2,n2,a3,n3)
    print "ans= "x," mod",N
