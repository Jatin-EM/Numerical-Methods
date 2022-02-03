import numpy as np
import matplotlib.pyplot as plt

x1=np.random.rand(1000)
x2=np.random.normal(0,1,1000)

plt.figure(1)
plt.subplot(211)
plt.hist(x1, density = 1, color ='green',alpha = 0.6)

plt.subplot(212)
plt.hist(x2, density = 1, color ='red',alpha = 0.7)
plt.xlim(-2,2)
                            
   