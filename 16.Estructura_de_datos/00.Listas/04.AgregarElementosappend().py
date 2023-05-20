# EN ESTE CAPITULO APREDEREMOS A AGREGAR ELEMENTOS A UNA LISTA USANDO EL METODO append()
# ESTE METODO NOS PERMITE AGREGAR NUEVOS ELEMENTOS AL FINAL DE UNA LISTA 
# SU SINTAXIS ES LS DIGUIENTE:
'''
nombre_lista.append(argumento a agregar)
'''

# EJEMPLO

letras = ['a', 'b', 'c', 'd']

#Imprimir la lista original
print(f'Lista original \n {letras}')

# Agregar otra letra
letras.append('e')
print(f'Lista con un elemento mas \n {letras}')

# Agregar un nuevo elemento
letras.append('f')
print(f'Lista con dod elemento mas \n {letras}')

# Tambien puedo agregar elemtos de cualquier tipo a la lista de python
letras.append(True)
letras.append(5)

print(f'Lista con 4 elentos de mas incluyendo boolean y number\n {letras}')
