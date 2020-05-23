import random 
"""
def codigo(numero):
    digitos = [1,2,3,4,5,6,7,8,9]
    codigo = []
    n = 1
    while n <=  numero:
        candidato = random.choice(digitos)
        while candidato not in codigo:
            codigo.append(candidato)  
            n += 1
    return codigo
"""
def codigo(numero):
    digitos = [1,2,3,4,5,6,7,8,9]
    codigo = []
    n = 1
    while n <=  numero:
        codigo.append(random.choice(digitos))  
        n += 1
    return codigo



def bienvenida():
    print('Bienvenido al juego MasterMind!\n')
    n = int(input('Dime con cuantas cifras  quieres jugar?\n'))
    print('Tienes que adivinar un codigo de',n,'Cifras\n')
    return n



def propuesta(numero):
    Propuesta = int(input('Ingresa un codigo, si te rindes preciona 0. \nQue Codigo propones?:  '))
    prop = []
    
    if Propuesta == 0:
        return [0]
    
    else:
        for i in range(numero,0,-1):
            prop.append(Propuesta // 10**(i-1))
            Propuesta = Propuesta % (10**(i-1))

        return prop