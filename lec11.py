import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate 

x=[0,1,2]
y=[1,2,4]
a=interpolate.CubicSpline(x, y)


z=np.arange(0,2,0.01 )
ai=a(z)
plt.figure(1)
plt.plot(z,ai,"r", label="Interpolation")
plt.plot(y,"o", label="given points")
plt.legend(loc="upper right")
plt.xlabel("x value")
plt.ylabel("interpolated function value")
plt.title("spline interpolation")
plt.show()
