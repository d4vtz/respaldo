import math
import numpy as np 
from sympy import Eijk as Levi_Civita



def LeviCivita():
    """
    Pseudotensor de levi civita E_{i,j,k,l} 
    
    Primero genera un tensor E_{i,j,k,l} lleno de ceros, despues 
    con ayuda de ciclos for anidados me genera todas las permutaciones
    y finalmente con ayuda de la funcion Levi_civita de sympy 
    le asigno un valor E_{i,j,k,l} = +1 a las permutaciones pares 
    y E_{i,j,k} = -1 a las permutaciones impares    
    
    Por ejemplo:
    i,k,j = 0,1,2
                [ 0.  0.  0.]   [ 0.  0. -1.]   [ 0.  1.  0.]
    E_{i,j,k} = [ 0.  0.  1.]   [ 0.  0.  0.]   [-1.  0.  0.]
                [ 0. -1.  0.]   [ 1.  0.  0.]   [ 0.  0.  0.]
    """
    lista = []
    for i in range(n):
        lista.append(n)

    E = np.zeros(tuple(lista))

    if n == 2:

        for i in range(n):
            for j in range(n):
                for k in range(3):
                    E[i,j] = Levi_Civita(i,j)
        return E
    
    elif n == 3:
    
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    E[i,j,k] = Levi_Civita(i,j,k)
        return E    

    elif n == 4:

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    for h in range(n):
                        E[i,j,k,h] = Levi_Civita(i,j,k,h)
        return E    






def productoVectorial(x,y):
    """ 
    Calculo del producto vectorial de dos vectores (x,y)

    Primero revisa si los vectores introducidos tienen la misma
    dimensión y esta es igual a 3. Si no se cumple la condición
    me regresa un mensaje de Error.
    Al cumplirse, me genera un vector z que por medio de un for 
    me genera sus componentes por medio de la expresión:

                C_{k} = A_{i}*B_{j}*E_{i,j,k}
    
    con ayuda del pseudotensor de Levi Civita.    
    """

    if len(x) != len(y) != 3:
        return 'Error: No se puede hacer el producto vectorial.'
    
    else:
        z = []
        
        for k in range(len(x)):
        
            producto = 0
            for i in range(len(x)):
                for j in range(len(x)):
                    producto = producto + x[i]*y[j]*LeviCivita()[i,j,k]
        
            z.append(producto)
        
    return z





def metricaM(n):
    """
    Metrica de Minkowsy de signatura (+,-,-,-)

                [ 1,  0,  0,  0]
        G[i,j]= [ 0, -1,  0,  0]
                [ 0,  0, -1,  0]
                [ 0,  0,  0, -1]
        """
    G=np.zeros((n,n))
    for i in range(n):
        if i == 0: 
            G[i,i] = 1
        else:
            G[i,i] = -1

    return G




def identidad(n):
    """
    Matriz Identidad
                [ 1,  0,  0,  0]
        I[i,j]= [ 0,  1,  0,  0]
                [ 0,  0,  1,  0]
                [ 0,  0,  0,  1]
        """
    I=np.zeros((n,n))
    for i in range(n):
        I[i,i] = 1 
        
    return I





def productoEscalarM(n,x,y):
    """
    Producto escalar de dos vectores en el espacio de
    Minkowsy. 
            a_[i]*b^[j] = a_[i]*G_[i,j]*b^[j]
    """
    prod = 0
    for i in range(n):
        for j in range(n):
                prod += x[i]*metricaM(n)[i,j]*y[j]
            
    return prod






def productoEscalar(n,x,y):
    """
    Producto escalar en el espacio Euclidiano
    """
    prod = 0
    for i in range(n):
                prod += x[i]*y[i]            
    return prod






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






def determinante(x):
    """
    Calculo del determinante de una Matriz
    """    
    fac = math.factorial(len(x))
    det = 0

    if len(x) == 2:
    
        for i in range(len(x)):
                for j in range(len(x)):
                    for n in range(len(x)):
                        for m in range(len(x)):
                            det += LeviCivita(2)[i,j]*x[m][i]*x[n][j]*LeviCivita(2)[m,n]
        return math.fabs(det/fac)

    
    elif len(x) == 3:
    
        for i in range(len(x)):
                for j in range(len(x)):
                    for k in range(len(x)):
                        for n in range(len(x)):
                            for m in range(len(x)):
                                for l in range(len(x)):
                                    det += LeviCivita(3)[i,j,k]*x[m][i]*x[n][j]*x[l][k]*LeviCivita(3)[m,n,l]

        return math.fabs(det/fac)

    elif len(x) == 4:
    
        for i in range(len(x)):
            for j in range(len(x)):
                for k in range(len(x)):
                    for s in range(len(x)):
                        for n in range(len(x)):
                            for m in range(len(x)):
                                for l in range(len(x)):
                                    for h in range(len(x)):                     
                                        det += LeviCivita(4)[i,j,k,s]*x[m][i]*x[n][j]*x[l][k]*x[h][s]*LeviCivita(2)[m,n,l,h]

        return math.fabs(det/fac)




def transpuestaMatrix(x):
    
    n = len(x)
    m = len(x[0])
    y = np.zeros((m,n))
    
    for i in range(n):
        for j in range(n):
            y[i,j]=x[j,i]
    return y

a=np.array([
            [1,2],
            [3,2]
])

z=determinante(a)