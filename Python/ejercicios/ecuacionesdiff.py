import numpy as np 
import matplotlib.pyplot as plt 

#   Datos
m = 1e-3
rho = 1000
g = 9.81
cA = 0.47
A = 1e-6

# Condiciones Iniciales
t = 0
u = 0

def f(t,u):
    return g - ((rho*A*cA)/(2*m))*u**2

tSol = [t]
uSol = [u]
dt = 0.05
tFin = 10

while t < tFin:
    u += f(t,u)*dt
    t += dt

    tSol.append(t)
    uSol.append(u)

#print(tSol,uSol)
plt.plot(tSol,uSol)
plt.show()