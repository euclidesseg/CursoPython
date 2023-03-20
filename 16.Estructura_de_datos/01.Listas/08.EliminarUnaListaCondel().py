# EN ESTE CAPITULO VEREMOS COMO ELIMINAR TODOS LOS DATOS DE UNA LISTA MEDIANTE LA INSTRUCCION del
# PODEMOS TAMBIEN ELIMINAR UNO O MAS ELEMENTOS ESPECIFICAOS 
# SU SINTAXIS ES LA SIGUIENTE:

'''
del nombre_lista            // elimina toda la lista
del nombre_lista[4]         // elimina la pocision numero 4 de la lista
del  nombre_lista[0 : 2]    // eliminara desde la pocision 0 hasta la 2
'''

# Ejemplo
jugadores = ['Crsitiano', 'Messi', 'Ramos', 'Ronaldiño', 'Benzema',]
print(f'Lista original \n {jugadores}')


# Eliminar el indice 4
del jugadores[4]
print(f'\n Lista eliminando el indice 4 \n {jugadores}')


# Eliminar desde la posicion 0 a la 2 tomara desde la pocision dos hacia a tras la el indice 2 no lo incluira
del jugadores[0 : 2]
print(f'\n Lista eliminando desde el indice 0 hasta el 2 \n {jugadores}')


# Eliminando toda la lista
del jugadores

print('\n lista eliminada ')