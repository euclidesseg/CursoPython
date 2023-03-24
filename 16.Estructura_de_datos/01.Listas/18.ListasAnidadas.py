# EN PYTHON ES POSIBLE TAMBIEN ALMACENAR LISTAS DENTRO DE LISTAS, PARA DE ESTGA MANERA OBTENER 
# UNA LISTA ANIDADA YA QUE LAS LISTAS TAMBIEN SON CONCIDERADAS UN TIPO DE DATOS:
    
    
# EJEMPLO

lista = [1, 'a', True, [1,2,3]]
print(f'Toda la lista \n {lista}')
# PARA ACCEDER A LOS ELEMENTOS DE LA LISTA ANIDADA LO HACEMOS DE LA SIGUIENTE MANERA


# Acedemos a la posicion 1 de la lista anidada
# y si tubiera asi otra lista anidada tambien podriamos acceder a ella con la misma sintaxis
print(f'La lista anidada es \n {lista[3]}')
print(f'Accedemos a la pocision 1 de la lista anidada \n {lista[3][1]}') 
