# EN ESTE CPAITLULO VEREMOS VER COMO ACCEDER A LOS ELEMENTOS DE UNA LISTA 
# PARA PODER MODIFICAR O ELIMINAR LOS ELEMENTOS

marcas =['Apol', 'Samsung', 'Xiaomi','Huawey']

print(f'\n La longitud de la lista len(marcas) es: {len(marcas)}')

# Imprimir toda la lista
print(marcas)

# Me imprimira solo el valor de la posision
print(marcas[2])

# Me imprimira la ultima posision de la lista
print(marcas[-1])


'''
Usando los Substrings
'''
# Me imprimira los elementos que esten entre el indice 1 y el indice 3
print(marcas[1:3])

# Me imprimira todos los elementos que esten antes del indice
print(marcas[:3])

# Me imprimira todos los elementos que esten despues del indice
print(marcas[2:])
