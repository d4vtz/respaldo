import funciones as fun
import informes as info

def tarifario():
    """ 
    El usuario ingresa la tarifa por segundo, cuántas
    comunicaciones se realizaron, y la duracion de cada
    comunicación expresada en horas, minutos y segundos. Como
    resultado se informa la duración en segundos de cada
    comunicación y su costo. 
    """
    tarifaLlamadaCorta = 0.15
    duracionTarifaCorta = 900
    tarifaLlamadaLarga = 0.30
    fun.tarifa(duracionTarifaCorta,tarifaLlamadaCorta,tarifaLlamadaLarga)

    numComunicaciones = int(input('Cuantas comuncaciones hubo?:  '))

    duracionTotal = 0
    duracionCorta = 0
    duracionLarga = 0
    
    costoTotal = 0
    costoTarifaCorta = 0
    costoTarifaLarga = 0
    
    for llamada in range(numComunicaciones):
        duracionLlamada = fun.llamadas(llamada)
        
        if duracionTarifaCorta > duracionLlamada:
            
            costoLlamada = duracionLlamada*tarifaLlamadaCorta
            
            costoTarifaCorta += costoLlamada
            costoTotal += costoLlamada
            
            duracionTotal += duracionLlamada
            duracionCorta += duracionLlamada

            info.informeLlamada(costoLlamada,duracionLlamada)

        else:
            costoLlamada = duracionLlamada*tarifaLlamadaLarga
            
            costoTarifaLarga += costoLlamada
            costoTotal += costoLlamada

            duracionTotal += duracionLlamada
            duracionLarga += duracionLlamada

            info.informeLlamada(costoLlamada,duracionLlamada)

    info.informeGeneral(costoTotal,duracionTotal,costoTarifaCorta,duracionCorta,costoTarifaLarga,duracionLarga)

tarifario()