# EN PYTNON ADEMAS DEL METODO  pop() TENEMOS EL METORO remove() PARA ELIMINAR UN ELEMENTO DE UNA LISTA 
# A DIFERENCIA DE pop() EN DONDE DEBEMOS ESPECIFICAR LA POCISION A ELIMINAR
# EL METODO remove() NOS PERMITE ESPECIFICAR EL ELEMENTO A ELIMINAR, LA SINTAXIS ES LA SIGUIENTE:
    
'''
nombre_lista.remove(elemento_a_eliminar)
'''

# EJEMPLO
jugadores = ['Crsitiano', 'Messi', 'Ramos', 'Ronaldiño', 'Benzema',]

print(f'Lista original \n {jugadores}')

# Eliminar un juegador especificando su nombre
jugadores.remove('Ramos')
print(f'Lista eliminando el elemento cuyo nombre es Ramos \n {jugadores}')

'''
NOTA: Si hay dos o mas elementos con el mismo nombre el metodo remove solo eliminara el primero que encuentre
para eliminar todos los elementos que sean iguales podemos recorrerlos mediante un siclo for 
para este caso el metodo tambien reconoce minusculas o mayusculas
'''