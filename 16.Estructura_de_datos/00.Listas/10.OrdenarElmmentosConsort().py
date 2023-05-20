# EN ESTE CAPITULO APRENDEREMOS A ORDENAR LOS ELEMENTOS DE UNA LISTA CON EL METOD sort()
# ESTE METODO NOS PERMITE ORDENAR UNA TANTO EN ACENDENTE COMO DESCENDENTE EL METODO sort() NOS PERMITE TRABAJAR CON UN ARGUMENTO 
# PARA INDEICAR  QUE LA LISTA SERA ORDENADA DE MANERA DESCENDENTE ( MAYOR-A-MENOR)
# SI LA LISTA ES DE STRINGS LOS ORDENA ALFABETICAMENTE Y SI ES NUMEROCA LO ORDENARA DESDE EL NUMERO MAYOR AL MENOR
# LA SINTAXIS PARA USAR EL METODO ES LA SIGUIENTE

'''
nombre_lista.sort(reverse = true)
'''
# Lista de strings
# ordenar decendentemente
jugadores = ['Crsitiano', 'Messi', 'Ramos', 'Ronaldiño', 'Benzema',]
print(f'Lista de strings original \n {jugadores}')
jugadores.sort(reverse = True)
print(f'Lista de strings ordenada desendentemente \n {jugadores}')

# Ordenar strings acendentemente
jugadores.sort(reverse = False)
print(f'Lista de strings ordenada acendentemente \n {jugadores}')


# lista de numeros
# Ordenar de manera descendente
numeros = [5,6,8,2,1,9,3]
print(f'Lista numerica original \n {numeros}')
numeros.sort(reverse = True)
print(f'Lista numerica ordenada desendente mente \n {numeros}')

# Ordenar acendentemente
numeros.sort(reverse = False)
print(f'Lista numerica ordenada acendentemente \n {numeros}')
