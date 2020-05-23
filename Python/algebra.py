import numpy as np 
#import matplotlib.pyplot as plt


def f(x):
    return x


suma = 0
n = 100
a = 0
b = 3

x = np.linspace(a,b,n)
delta = (b-a)/n
for i in range(len(x)): 
    suma += f(a+i*delta)*(x[i]-x[i-1])

print(suma)