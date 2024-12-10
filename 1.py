import numpy as np
import matplotlib.pyplot as plt
x= np.arange(0,3*np.pi, 0.1) #start, stop, stepsize
y=np.tan(x)
plt.plot(x,y)
plt.show() 