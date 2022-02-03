def nlarge(a,n):
    j=0
    out=[]
    for k in range(n):
        x=a[0]
        for i in range(len(a)):
            if a[i]>x:
                x=a[i]
                j=i
        out=out+[x]
        a[j]=0
    print("first",n,"largest numbers in the array are",out)
    return(out)


