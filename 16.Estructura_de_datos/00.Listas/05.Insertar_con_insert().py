# EN ESTA OCACION VEREMOS COMO AGREGAR ELEMENTOS A UNA LISTA CON EL METODO insert()
# ESTE METODO A DIFERENCIA DE append() NOS PERMITE INDICAR LA POSICION EXACTA  DONDE QUEREMOS AGREGAR EL NUEVO ELEMENTO
# LA SINTAXIS ESLA SIQUIENTE:

'''
nombre_lista.insert(2, 'Cristiano')

como vemos sismpre debemos pasarle dos parametros siendo el primero un numero entero obligatoriamente
y el segundo el valor que deseamos agregar a la lista 
'''    

jugadores = ['Messi', 'Ramos', 'Ronaldiño', 'Benzema',]
print(f'Lista Original \n {jugadores}')

# Insertar al inicio de la lista esta accon lo que hara sera correr todos los demas valores
# hacie el final agregando un nuevo segmento de memoria a la lista
jugadores.insert(0, 'Cristiano')
print(f'Lista Con nuevo valor al inicio \n {jugadores}')

# Insertar un nuevo valor en la pocision numero 2 esta accion movera los elementos desde la pocision dos hacia el final
# creando una nueva pocision
jugadores.insert(2, 'David Becakn')
print(f'Lista Con nuevo valor en el indice 2 \n {jugadores}')

'''
cuando tengamos una posicion que supere la canridad de elementos que tenemos en la lista
lo unico que hara python sera agregar el elemento al fial de la lista
Ej: jugadores.insert(100, 'Pele')
'''
jugadores.insert(100, 'Pele')
print(f'Lista Con nuevo valor al final con un indice superior \n {jugadores}')
