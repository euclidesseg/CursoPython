# EN ESTE CAPITULO APRENDEREMOS A CONCATENAR LISTAS USANDO EL METODO extend()
# EL METODO extend() NOS PERMITE CONCATENAR DOS O MAS LSITAS Y AGREGAR VARIOS ELEMENTOS A UNA LSITA
# COMO ELEMENTOS INDIVIDUALES A PARTIR DE UNA SECUENCIA, SU SINTAXIS ES LA SIGUIENTE

'''
nombre_lista.extend(objeto_iterable)    // el objeto iterable sera la lista que se quiere concatenar
nombre_lista.extends(range( 0 : 4 ))   // tambie podemos usar la clase range
'''
# Primera lista 
jugadores = ['Crsitiano', 'Messi', 'Ramos', 'Ronaldiño', 'Benzema',]

# Lista para concatenar
jugadoresDos = ['Caca', 'James', 'Neymar', 'Luis', 'Marcelo']

print(f'\n Lista original \n {jugadores}')

# Concatenar con range esta forma concatenara solo valores numericos 
# ya que la clase range genera solo secuencia de numeros
jugadores.extend(range(len(jugadores)))

# Imprimir a jugadores con su concatenacion
print(f'\n lista concatenada \n {jugadores}')

# concatenar con la segunda lista
jugadores.extend(jugadoresDos)

# Imprimir a jugadores con la doble concatenacion
print(f'\n lista concatenada con range y con jugadoresDos \n {jugadores}')