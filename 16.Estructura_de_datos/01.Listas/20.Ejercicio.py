'''
Crear una matriz llenando dinamicamente sus elementos tanto y mostrarla 
al final en formato de grafica
el usuario debera ingresar cuantas filas y columnas tendra la matriz
'''
filas = int(input('Cuantas filas tendra la matriz?'))
columnas = int(input('Cuantas columnas tendra la matriz?'))

fila = []

for i in range(filas):
    columna = []
    for j in range(columnas):
        columna.append(int(input(f'introduce un elemento a la fila numero {i + 1}\n')))
    fila.append(columna)

print('\nImprimiento la matris dinamicamente recorriendo las listas internas')
for i in range(len(fila)):
    for j in range(len(fila[i])):
        print(f'[{fila[i][j]}]' , end = "")
    print()
print('Fin')