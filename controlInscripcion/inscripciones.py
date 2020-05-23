import interface as inter 


def inscripcion():
    print('Bienvenido al sistema de registro de usuarios.')
    print('Ingrese la opcion que desee\n')

    print('1) Inscribir usuarios')
    print('2) Eliminar usuarios')
    print('3) Ver lista')
    opcion = int(input())

    if opcion == 1:
        lista = inter.inscribirUsuario()
    elif opcion == 2:
        lista = inter.borrarUsuario(lista)
    else:
        print(lista)


inscripcion()