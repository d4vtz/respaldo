import random

def codigo(numero):
    digitos = [1,2,3,4,5,6,7,8,9]
    codigo = []
    n = 1
    while n <=  numero:
        codigo.append(random.choice(digitos))  
        n += 1
    return codigo

print(codigo(4))