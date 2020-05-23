import numpy as np  

def f(x):
    return x**3 - x**2 + 4*x - 5

def F(x):
    return 3*x**2 - 2*x + 4

def Newton(x):
    tol_error = 1e-10
    tol_iteraciones = 20
    cont = 1
    if F(x) != 0:
        while cont < tol_iteraciones:
            
            xold = x
            x = x - f(x)/F(x)
            error = np.fabs((x-xold)/x)
            
            if error < tol_error:
                print('La raiz es ',x,' con ',cont,'iteraciones y valor de la funcion ',f(x))
                break
            
            cont += 1

Newton(3)
