import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

def f(x):
    y=np.sin(np.cos(np.exp(x)))
    return(y)

def ff(x):
    yy=-1*np.cos(np.cos(np.exp(x)))*(np.sin(np.exp(x)))*(np.exp(x))
    return(yy)

def small(a,b):
    if abs(f(a))>abs(f(b)):
        return (b)
    else:
         return(a)


##BISECTION
a=-1
b=1
xi=-1
x=small(a,b)
e=x
eb=[]  #error
en=[]

for i in range (100):
    #Bisection Method
    if f(a)*f(0.5*(a+b))<=0:
        b=0.5*(a+b)
    elif f(b)*f(0.5*(a+b))<0:
            a=0.5*(a+b)
    e=small(a,b)-x
    x=small(a,b)
    eb=eb+ [abs(e)]
    
    #Newton Method
    xxi=xi-f(xi)/ff(xi)
    en=en + [abs(xxi-xi)]
    xi=xxi
  
plt.figure(1)
plt.plot(eb, 'r', label="bisection")
plt.plot(en, 'b', label="Newton's Method")
plt.xlabel('iterations')
plt.ylabel('error')
plt.legend(loc="upper right")
plt.title('Comparison of Bisection and Newton method')
plt.show()


#using scipy library
x_bisection_sp=optimize.bisect(f,a,b)
x_newton_sp=optimize.newton(f,xi,ff)
  
print("root obtained from implemented bisection method is",x,"in iterations",1+i)
print("root obtained by using Scipy library bisection",x_bisection_sp)
print("root obtained from implemented Newton ", xi,"in iterations",1+i)
print("root obtained by using Scipy library Newton method",x_newton_sp)