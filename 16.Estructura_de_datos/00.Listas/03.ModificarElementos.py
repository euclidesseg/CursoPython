# EN ESTA OCASION VEREMOS COMO MODIFICAR ELEMENTOS DE UNA LISTA EN PYTHON

vocales =['a', 'e', 'i', 'o', 'u']

print(f'\n Lista original \n {vocales}')

# Modificar la posision 1
vocales[1] = 'x'
print(f'\n Lista modificada \n {vocales}')

# Modificar 2 o mas elementos simultaneamente usando substring
vocales[2:4] = ['m', 's']
print(f'\n Lista modificada en un rango \n {vocales}')

# Si el numero de valores que yo voy a agregar es mayor que el rango de pocisiones lo que hace python 
# es agregar una nueva posision a la lista y si hay elementos luego del rango maximo los corre hacia el final
# en este caso correra a la u a una pocision numero 6 y agregar la letra r a la pocision 5 o indice 4
vocales[2:4] = ['m', 's', 'r']
print(f'\n Lista modificada en un rango \n {vocales}')

# Modifica el primer elemento y elimina el resto
vocales[:] = 'x'
print(vocales)
