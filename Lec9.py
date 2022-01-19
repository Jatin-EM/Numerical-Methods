def f_in(x): #function whose integral needs to be evaluated
    return 10-3*x*x

iu=3 #upper limit
il=-1 #lower limit
A=0 #integral
n=4 #interpolation points
iw=(iu-il)/n
j=1


for j in range(n):
 if j%2==1:
   A=A+4*f_in(il+iw*j)
 else:
   A=A+2*f_in(il+iw*j)
   
A=A+f_in(il)+f_in(iu)
A=A*(iu-il)/(3*n)
print("integral is ", A)
