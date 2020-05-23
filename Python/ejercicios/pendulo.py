import numpy as np 
import matplotlib.pyplot as plt 

#   Datos
l = 1
g = 9.81

#   Condiciones iniciales
t = 0
tFin = 10
theta0 = 0
omega0 = 0.5
dt = 0.05

u = np.array([theta0, omega0])

#   Campo de direcciones
def F(t,u):
    return np.array([u[1], -(g/l)*np.sin(u[0])])

tSol = [t]
thetaSol =[u[0]]
omegaSol =[u[1]]


while t < tFin:
    u = u + F(t,u)*dt
    t += dt 
    thetaSol.append(u[0])
    omegaSol.append(u[1])
    tSol.append(t)
    
#plt.plot(tSol,thetaSol)
#plt.plot(tSol,omegaSol,'--')
#plt.plot(thetaSol,omegaSol,'r')
#plt.show()

import matplotlib.animation as animation

fig = plt.figure()
ax = fig.gca()

def actualizar(i):
    ax.clear()
    plt.plot(l*np.sin(thetaSol[i]),-l*np.cos(thetaSol[i]),'ro')
    plt.title(str(round(tSol[i],3)))
    plt.xlim(-l,l)
    plt.ylim(-l,0)

ani = animation.FuncAnimation(fig,actualizar,range(len(tSol)))
plt.show()








