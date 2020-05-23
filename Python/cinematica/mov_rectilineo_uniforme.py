import numpy as np
import matplotlib.pyplot as plt 

t_1 = 10
t_0 = 0
N = 500
delta_t = (t_1-t_0)/N

t = np.linspace(t_0,t_1,N)
x = np.zeros(N)
x_vel = np.zeros(N)

def V(t,x):
    return 1

def Vel(t,x):
    return t*np.math.cos(t)


x[0]=1
for n in range(1,N):
    x[n] = x[n-1] + V(t[n-1],x[n-1])*delta_t
    x_vel[n] = x_vel[n-1] + Vel(t[n-1],x_vel[n-1])*delta_t


fig, ax = plt.subplots()
fig.suptitle('xn(tn)=xn(tn)+v(tn,xn)deltat', fontsize=15)
ax.plot(t,x,color="red", label="V(t,x)=1.0")
ax.plot(t,x_vel,color="blue", label="V(t,x)=t cos(t)")
ax.legend(loc="best", title="Velocidades", frameon=False)

plt.show()




