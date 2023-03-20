# EN ESTE CAPITULO APRENDEREMOS A BUSCAR UN ELEMENTO DENTRO DE UNA LSITA USANDO EL METODO index() 
# EL METODO idex() NOS DEVUELVE UN VALOR ENTERO QUE INDICA LA POSICION DEL VALOR ENCONTRADO
# NOS PERMITE TRABAJAR CON UN ARGUMENTO Y MAXIMO TRES ARGUMENTOS
# SU SINTAXIS ES LA SIGUIENTE:
    
'''
nombre_lista.index(argumento)                    //indica solo argumento y se buscara en toda la lista
nombre_lista.index(argumento,  inicio)          // indica el argumento y desde que pocision quiero bucar
nombre_lista.index(argumento, inicio, final)   //  indica el argumento desde y hasta que pocision quuiero buscar
'''

# lista 
jugadores = ['Crsitiano', 'Messi', 'Ramos', 'Ronaldiño', 'Benzema',]
print(f'lista original \n {jugadores}')

# Buscar a benzemas y guardarle eun una variable
print('Buscar a un criterio y guardarle eun una variable')
criterio = jugadores.index('Benzema')
print(f'Resultado del criterio buscado \n {jugadores[criterio]}')

'''
se imprimo poniendo como pocision el criterio porque el metodo index nos
debuelve un numero entero
'''