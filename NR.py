def input(x):  #input function
    return x*x-10

def derr_in(x):  #derrivative of input function
    return 2*x

def newton(x): #function for calculation of x(i+1) using newton raphson method
    return (x-input(x)/derr_in(x))
x=4   #initial guess
i=100 #iterations
for i in range(100):
   x=newton(x)

print("The value of the root is : ",x)
