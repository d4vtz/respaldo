#       Modulos

def tiempoSegundos(horas,minutos,segundos):
    '''
    Funcion que devuelve en segundos un tiempo dado en horas:minutos:segundos.
    '''
    return segundos + minutos*60 + horas*60*60




def tiempoCompleto(segundos):
    '''
    Funcion que devuelve en horas:minutos:segundos un tiempo dado en segundos.
    '''
    horas = segundos // 3600
    segundos = segundos % 3600
    minutos = segundos // 60
    segundos = segundos % 60 
    return horas,minutos,segundos




def divisa(cantidad):
    '''
    Convierte una cantidad decimal en pesos y centavos
    '''
    pesos = int(cantidad // 1)
    centavos = int(round(cantidad % 1,2)*100)  
    return pesos, centavos




def tarifa(duracionTarifaCorta,tarifaLlamadaCorta,tarifaLlamadaLarga):
    horas, minutos, segundos = tiempoCompleto(duracionTarifaCorta)

    print('La tarifa de llamadas cortas es de $',tarifaLlamadaCorta,'pesos con una duración de ',horas,'horas con',minutos,'minutos y',segundos,'segundos.')

    print('\nLa tarifa de llamadas largas es de $',tarifaLlamadaLarga,'pesos.\n')




def llamadas(llamada):
    print('\n\tLlamada numero',llamada+1,'\n')

    horas = int(input('Cuantas horas duro la llamada?: '))
    minutos = int(input('Cuantos minutos duro la llamada?: '))
    segundos = int(input('Cuantos segundos duro la llamada?: '))
    duracionLlamada = tiempoSegundos(horas,minutos,segundos)
    return duracionLlamada
