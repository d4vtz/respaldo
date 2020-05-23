
def inscribirUsuario():

    print('Dime la lista de matriculas de inscripcion')
    print('Para salir presiona: q')
    lista = []

    alumno = input('Dime la matricula del usuario: ')
    while alumno != 'q':

        if alumno not in lista:
            lista.append(alumno)
            alumno = input('Dime la matricula del usuario: ')
        else:
            alumno = input('Matricula repetida. Digite otra: ')

    return lista

def borrarUsuario(lista):
    usuario = input('Dime a que usuario quieres eliminar de la lista:  ')
    newLista = []
    for objeto in lista:
        if objeto != usuario:
            newLista.append(objeto)
        else:
            continue
    return newLista


