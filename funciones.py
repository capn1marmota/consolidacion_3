#en este archivo se encuentran las funciones que se utilizan en el programa

def hacer_grandioso(magos):
    for mago in magos:
        magos[magos.index(mago)] = f'El gran {mago}'
    return magos

def imprimir_nombres(lista):
    for nombre in lista:
        print(nombre)
