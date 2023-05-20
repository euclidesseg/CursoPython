#La comprensión de listas es una construcción en Python que nos 
# permite crear listas a partir de otras listas, tuplas y cualquier iterable.

lista = []

# Aqui vemos una forma normal de crear una lista en python mediante un iteracion
for i in range(0, 10):
    lista.append(i)
print(lista)


# Aqui acavamos de ver una forma mas eficas y rapida de crear una lista apartir de un iterable
# de esta menrar reducimos el tiempo de ejecucion
lista2 = [numero for numero in range(0,10)]
print(lista2)



# en donde el primer datos ( numero ) sera el valor que se va a ingresar en nuestra lista cada vez que se 
# itere el rango en nuestra expresion, 

# seguido d eese primer valor ira una expresion de un siclo forLup y opcional mente una condicion
# que estara en el punto dos de esta sesion

