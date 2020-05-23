        ####    Metodo de la bisección  ####
        ####################################
'''
Este programa realiza el calculo de la raiz de una función f(x)=0,
Ocupa el hecho de que en una función continua en un intervalo [a,b]
de modo que si evaluamos f(a)F(b) < 0 entonces tenemos una raiz 
dentro de ese intervalo.
'''

#   Función a resolver
def f(x):
    return x**2-9
#   Definimos el mensaje a mostrar cuando se encuentre la solución
def mensaje(raiz,iteracion):
    print('La raiz es: ',raiz,' con ',iteracion,' iteraciones')

#   Definición del intervalo [a,b]
a = 0
b = 9

#   Parametros (# de iteraciones max, tolerancia max de error)
tol_iteracion = 50
tol_error = 1e-3

#   Inicio del ciclo iterativo
cont = 0
while cont < tol_iteracion:
    x = (a+b)/2

    if f(x)*f(b) < 0:
        a = x

    elif f(a)*f(x) < 0:  
        b = x

    else:
        if f(a) == 0:
            mensaje(a,cont)
            break
        else:
            mensaje(b,cont)
            break
    
    if b - a < tol_error:
        mensaje(x,cont)
        break
    cont += 1