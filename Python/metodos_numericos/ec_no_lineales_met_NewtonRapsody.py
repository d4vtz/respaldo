import numpy as np

def F(x):
    F_1 = x[0]**3 + 3*x[1]**2 - 21
    F_2 = x[0]**2 + 2*x[1] + 2
    return np.array([F_1,F_2])


def dF(x):
    dF_00 = 3*x[0]**2
    dF_01 = 6*x[1]
    dF_10 = 2*x[0]
    dF_11 = 2
    return np.array([[dF_00,dF_01],
                     [dF_10,dF_11]])

x = np.array([10,10])
tol_iteracion = 30
tol_error = 1e-6
cont = 0

while cont < tol_iteracion:
    xold = x
    Jac_F = np.linalg.inv(dF(x))
    x = x - np.dot(Jac_F,F(x))
    error = np.linalg.norm(x - xold)
    
    if error < tol_error:
        print(cont,x)
        break   
        
    cont += 1