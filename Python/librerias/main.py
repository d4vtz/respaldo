#Programa Principal

#importación
from codigo import gradiente as grad
import matplotlib.pyplot as plt 
import numpy as np 


def f(x,y):
    return -1/np.sqrt(x**2 + y**2)

X,Y,fx,fy = grad.gradiente2D(f,-2,2,10,-2,2,10)

plt.quiver(X,Y,fx,fy)
plt.show()
