# EN PYTHON ES POSIBLE ELIMINAR ELEMENTOS DE UNA LISTA USANDO EL METODO pop()
# ESTE METODO SI NO SE LE MANDA UN PARAMETRO INDICANDO LA POCISION DEL DELEMETO A ELIMINAR ELIMINARA EL ULTIMO ELEMENTO DE LA LISTA
# ESTE METODO SIEMPRE NOS RETORNA EL ELEMENTO QUE SE ACABA DE ELIMINAR
# LA SINTAXIS ES LA SIGUIENTE:

'''
nombre_lista.pop()   // elimina el ultimo
nombre_lista.pop(3) //  elimina el valor en el indice numero3
'''
# EJEMPLO
jugadores = ['Crsitiano', 'Messi', 'Ramos', 'Ronaldiño', 'Benzema',]
print(f'Lsita original \n {jugadores}')

# eliminar el ultimo elemento de la lista
jugadores.pop()
print(f'Lsita eliminando el ultimo elemento \n {jugadores}')

# Eliminar un elemento especifico
jugadores.pop(1)
print(f'Lsita eliminando el elemento de la pocision 1 \n {jugadores}')

'''
si por error le indico eliminar un valor que es mayor al numero de indice
el programa me retornara indexerror pop index out of range 

el indice indicago se salio del rango de la pocision maxima
'''
