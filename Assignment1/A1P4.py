import time
t1=time.time()
def fib(n):
    
    a=0
    b=0
    c=1
    for i in range(n-2):
        a=b
        b=c
        c=a+b
    print("nth fibonacci number is",c)
    return(c)
       
fib(1000)
t2=time.time()
print("runtime=",t2-t1)