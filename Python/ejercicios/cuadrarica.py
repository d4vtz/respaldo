import math
import numpy as np




print('\n')
print('     Dime la ecuación cuadratica a resolver... \n')
print('         De la forma a*x^2 +b*x + c = 0 \n')


a = float(input('a:   '))
b = float(input('b:   '))
c = float(input('c:   '))


if a == 0:
    x = -c/b 
    print('La ecuación solo tiene una solución:\n')
    print('x = ',x)

else: 
    det = b**2 - 4*a*c
    if det >= 0:
        x1 = (-b + np.sqrt(det))/(2*a)
        x2 = (-b - np.sqrt(det))/(2*a)
        
        print('Las raices son reales: \n')
        print(x1, ' ' ,x2)
    
    else:
        real = (-b)/(2*a)
        imaginario = np.sqrt(-det)/(2*a)
        x1 = complex(real,imaginario)
        x2 = complex(real,(-1)*imaginario)
        print('Las raices son complejas: \n')
        print(x1, x2)