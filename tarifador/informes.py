#       informes
import funciones as fun 


def informeLlamada(costo,duracion):
    pesos, centavos = fun.divisa(costo)
    hora, minuto, segundo = fun.tiempoCompleto(duracion)

    print('\nLa duración de la llamada:',hora,'horas con',minuto,'minutos y',segundo,'segundos.')
    print('Costo total de la llamada: $',pesos,'pesos con ',centavos,'centavos\n')



def informeGeneral(costoTotal,duracionTotal,costoCorta,duracionCorta,costoLarga,duracionLarga):
    pesosCorta, centavosCorta = fun.divisa(costoCorta)
    pesosLarga, centavosLarga = fun.divisa(costoLarga)
    pesos, centavos = fun.divisa(costoTotal)

    horaCorta, minutoCorta, segundoCorta = fun.tiempoCompleto(duracionCorta)
    horaLarga, minutoLarga, segundoLarga = fun.tiempoCompleto(duracionLarga)
    hora, minuto, segundo = fun.tiempoCompleto(duracionTotal)

    print('\nCosto total de todas las llamada cortas: $',pesosCorta,'pesos con ',centavosCorta,'centavos con una duración total de:',horaCorta,'horas con',minutoCorta,'minutos y',segundoCorta,'segundos.')

    print('Costo total de todas las llamada largas es de $',pesosLarga,'pesos con ',centavosLarga,'centavos con una duración total de:',horaLarga,'horas con',minutoLarga,'minutos y',segundoLarga,'segundos.')

    print('Costo total de todas las llamada es de $',pesos,'pesos con ',centavos,'centavos con una duración total de:',hora,'horas con',minuto,'minutos y',segundo,'segundos.')
