import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,2,100)
y1= np.sin(t)
x1=np.cos(t)

y1= np.sin(t)
x1=np.cos(t)

y2= np.sin(2*t)
x2=np.cos(3*t)

y3=abs(np.cos(4*t))*np.sin(t)
x3=abs(np.cos(4*t))*np.cos(t)

plt.figure(1)
plt.plot(x1,y1,"b",label="a")
plt.plot(x2,y2,"g",label="b")
plt.plot(x3,y3,"r",label="c")
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc="upper right")
plt.title('Problem 3')
plt.show()

