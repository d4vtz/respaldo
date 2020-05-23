import modulo as mod

def juego():
    
    n = mod.bienvenida()
    codigo = mod.codigo(n)
    propuesta = mod.propuesta(n)    

    intentos = 1

    while propuesta != codigo and propuesta != [0]:
        
        aciertos = 0
        coincidencias = 0

        for i in range(len(codigo)):

            if propuesta[i] == codigo[i]:
                aciertos += 1

            elif propuesta[i] in codigo:
                coincidencias += 1
        
        print('\nTu propuesta',propuesta,'tiene',aciertos,'aciertos y',coincidencias,'coincidencias\n')
        propuesta = mod.propuesta(n)
        intentos +=1

        


    if propuesta == codigo:
       print('Felicidades, adivinaste el codigo en',intentos,'intentos')
    else:
        print('Lo siento, el codigo es',codigo,'!suerte para la proxima!')
juego()