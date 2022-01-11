def f_in(x):
    return 10-x*x

iu=2
il=-2
A=0
n=100
iw=(iu-il)/n
j=1


x=il
while(iw*j+il<iu):
  A=A+abs(f_in(il+iw*j)*iw)
  j=j+1
A=A+0.5*(f_in(iu)+f_in(il))
print("area is ",A)
