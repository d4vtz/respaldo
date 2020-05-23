import numpy as np 
import matplotlib.pyplot as plt 

#   Datos
q = 10
m = 3

#   Condiciones iniciales
t = 0
tFin = 5
dt = 0.0001

x, y, z = 1, -5, 0
Vx, Vy, Vz = 9, 1, -2

u = np.array([x, y, z, Vx, Vy, Vz])

#   Campo de direcciones
def F(t,u):
    B = np.array([0,0,5])
    return np.array([
            u[3],
            u[4],
            u[5],
            (q/m)*(np.cross([u[3],u[4],u[5]],B)[0]),
            (q/m)*(np.cross([u[3],u[4],u[5]],B)[1]),
            (q/m)*(np.cross([u[3],u[4],u[5]],B)[2]),        
                    ])

t_Solve = [t]
x_Solve =[u[0]]
y_Solve =[u[1]]
z_Solve =[u[2]]

a_Solve =[u[3]]
b_Solve =[u[4]]
c_Solve =[u[5]]

while t < tFin:
    u = u + F(t,u)*dt
    t = t + dt 
    x_Solve.append(u[0])
    y_Solve.append(u[1])
    z_Solve.append(u[2])

    a_Solve.append(u[3])
    b_Solve.append(u[4])
    c_Solve.append(u[5])

    t_Solve.append(t)
    
#from mpl_toolkits.mplot3d import Axes3D

#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
plt.plot(t_Solve,z_Solve)
plt.show()


#import matplotlib.animation as animation

#fig = plt.figure()
#ax = fig.gca()

#def actualizar(i):
#    ax.clear()
#    plt.plot(x_Solve[i],y_Solve[i],'ro')
#    plt.title(str(round(t_Solve[i],3)))
#    plt.xlim(-1,1)
#    plt.ylim(-1,1)

#ani = animation.FuncAnimation(fig,actualizar,range(0,len(t_Solve),50))
#plt.show()
