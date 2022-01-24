x_in=[0,1,2] #x input
y_in=[1,2,4] #y_input

x=1.5
y=0


#Lagrange interpolation
for i in range(len(x_in)):
    l=1
    for j in range(len(x_in)):
        if (i!=j):
            l=l*((x-x_in[j]))/(x_in[i]-x_in[j])
    y=y+l*y_in[i]
    


print("value of function at x by interpolation is",y)
yy=2**x
print("value of function at x is",yy)
