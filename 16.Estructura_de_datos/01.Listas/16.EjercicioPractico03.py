# DADA UNA LISTA SE PIDE ELIMINAR EL ULTIMO Y PRIMER ELEMENTO 
# IMPRIMIR EN CONSOLA LA LISTA CON LOS ELEMENTOS NO ELIMINADOS 
# Y UNA LISTA CON LOS ELEMENTOS ELIMINADOS

numeros = [9,1,2,3,4,5,26]
lista_eliminados = []

for numero in range(len(numeros)):
    if(numero == 0):
        lista_eliminados.append(numeros.pop(0))
    elif(numero == len(numeros)):
        lista_eliminados.append(numeros.pop())
    else:pass

print(numeros)
print(lista_eliminados)

