import numpy as np 

def f(x):
    return x**3 - x**2 + 4*x - 5

def Secante(x0,x1):

    tol_error = 1e-10
    tol_iteraciones = 20
    cont = 1

    while cont < tol_iteraciones:
        xold = x1
        x1 = x1 - f(x1)*((x1-x0)/(f(x1)-f(x0)))
        x0 , x1 = x1, x0
        x1 = x1 - f(x1)*((x1-x0)/(f(x1)-f(x0)))
        error = np.fabs((x1-xold)/x1)
            
        if error < tol_error:
            print('La raiz es ',x1,' con ',cont,'iteraciones y valor de la funcion ',f(x1))
            break
            
    cont += 1

Secante(0,1)