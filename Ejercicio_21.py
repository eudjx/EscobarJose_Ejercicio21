import numpy as np
import matplotlib.pylab as plt

#Primero
x=np.linspace(-2*np.pi, 2*np.pi, 1000)
plt.plot(x, np.sin(x))
plt.show()