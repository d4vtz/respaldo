import numpy as np 
import matplotlib.pyplot as plt


def F(t):
    return np.array([np.cos(t),np.sin(t)])

t = np.linspace(0,10,30)


plt.plot(t,F(t))
plt.show()