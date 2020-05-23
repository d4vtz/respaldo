import numpy as np

def productoMatrix(a,b):
    """
    Producto de Matrices (m x n) = (m x l)(l x n)
    """
    c = np.zeros((len(a),len(b[0])))
 
    for i in range(len(a)):
        for j in range(len(b[0])):    
            for k in range(len(b)):
                c[i,j] += a[i,k]*b[k,j]
    return c

def productoMx(M,x):
    """
    Producto de Matrices (m x n) = (m x l)(l x n)
    """
    c = np.zeros((len(x)))
 
    for i in range(len(x)):
        for j in range(len(M[0])):    
            c[i] += M[i,j]*x[j]
    return c



def composicion(A):
    D = np.zeros((len(A),len(A)))
    T = np.zeros((len(A),len(A)))
    
    for i in range(len(A)):
        for j in range(len(A)):
            if i == j:
                D[i,j] = 1/A[i,j]
            else:
                T[i,j] = -A[i,j]
    return [D,T]


def iteracion(A,b):
    
    if len(A) == len(b):
        max_iteracion = 10
        Dinv = composicion(A)[0]
        LU = composicion(A)[1]
        T = productoMatrix(Dinv,LU)
        C = productoMx(Dinv,b)

        x = np.zeros(len(b))
        y = []
        tolerancia = 0.05       
        cont = 0
        while cont < max_iteracion:
            x = productoMx(T,x) + C
            y.append(x)
            print(x)
            cont += 1    
#            if y[cont+1]-y[cont] < telerancia:
#                return x   
    else:
        print('Las dimenciones de la matriz A y el vector b no coinciden')    



A = np.array([
            [8,2,0],
            [2,9,1],
            [1,1,7]
])

b = np.array([1,2,3])

iteracion(A,b)