from funciones import *

# Crear una lista de nombres

magos = ['Harry Houdini', 'David Blaine', 'Teller']
cientificos = ['Newton','Hawking','Einstein']
otros = ['Messi', 'Pele', 'Juanes']

#hacemos grandiosos a los magos

lista = hacer_grandioso(magos)

#pero no contentos con eso, reunimos todos los nombres

gran_lista = [magos, cientificos, otros]

imprimir_nombres(gran_lista)
