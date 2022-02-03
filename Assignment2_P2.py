import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

def f(x):
    y=np.exp(x)
    return(y)

a=0 #lower limit of integration
b=1 #upper limit of integration
n= 100 #max iterations

i_lha=[]
i_rha=[]
i_mpa=[]
i_smpsna=[]
i_tpzda=[]


for i in range(n):
    i_lh=0
    i_rh=0
    i_mp=0
    i_tpzd=0
    i_smpsn=0
    for j in range(i+1):
        h=(b-a)/(i+1)
        #left hand rule
        i_lh=i_lh+h*f(a+j*h)
        i_rh=i_rh+h*f(a+(1+j)*h)
        i_mp=i_mp+h*f(a+(0.5+j)*h)
        i_tpzd=i_tpzd+h*f(a+(1+j)*h)
        if j<i:
           i_smpsn=i_smpsn+2*(h/3)*(f(a+(1+j)*h))
           if j%2==0:
              i_smpsn=i_smpsn+2*(h/3)*(f(a+(1+j)*h))
    i_tpzd=i_tpzd+0.5*h*(f(a)-f(b))
    i_smpsn=i_smpsn+(h/3)*(f(a)+f(b))
    i_lha=i_lha+[i_lh]
    i_rha=i_rha+[i_rh]
    i_mpa= i_mpa+[i_mp]
    i_smpsna=i_smpsna+[i_smpsn]
    i_tpzda=i_tpzda+[i_tpzd]
    
e_lhr=np.subtract(([0]+i_lha),(i_lha+[0]))
e_rhr=np.subtract(([0]+i_rha),(i_rha+[0]))
e_mp=np.subtract(([0]+i_mpa),(i_mpa+[0]))
e_tpzd=np.subtract(([0]+i_tpzda),(i_tpzda+[0]))
e_smpsn=np.subtract(([0]+i_smpsna),(i_smpsna+[0]))
print()
print("Integral using Left rule",i_lh)
print("Integral using right rule",i_rh)
print("Integral using midpoint rule",i_mp)
print("Integral using Trapezoid rule",i_tpzd)
print("Integral using simpson rule",i_smpsn)
print()
plt.figure(1)
plt.plot(e_lhr[1:-1], 'r', label="Left hand rule")
plt.plot(e_rhr[1:-1], 'g', label="right hand rule")
plt.plot(e_mp[1:-1], 'b', label="Mid point rule")
plt.plot(e_tpzd[1:-1], 'm', label="Trapezoid rule")
plt.plot(e_smpsn[1:-1], 'k', label="Simpson rule")
plt.xlabel('iterations')
plt.ylabel('error')
plt.legend(loc="upper right")
plt.title('Comparison of various methods of numerical integration')
plt.show()

ii=np.arange(0, n+1,1)
xii=np.multiply(ii,(b-a)/n)
y=f(xii)
i_tpzd_np=np.trapz(y,xii)
i_smpsn_sp=integrate.simpson(y, x=None, dx=(b-a)/n, even='avg')
i_romb=integrate.romberg(f,a,b)
i_quad=integrate.fixed_quad(f, a, b,n=5)

print("Integral using Numpy library, Trapezoid rule",i_tpzd_np)
print("Integral using Scipy library, simpson rule",i_smpsn_sp)
print("Integral using Scipy library, Romberg rule", i_romb)
print("Integral using Scipy library, Gauss Quadrature rule",i_quad)