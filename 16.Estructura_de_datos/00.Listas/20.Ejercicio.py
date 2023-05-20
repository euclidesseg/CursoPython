'''
Crear una matriz llenando dinamicamente sus elementos y mostrarla 
al final en formato de grafica
el usuario debera ingresar cuantas filas y columnas tendra la matriz
'''
filas = int(input('Cuantas filas tendra la matriz?'))
columnas = int(input('Cuantas columnas tendra la matriz?'))

matrix = []

for i in range(filas):
    columna = []
    for j in range(columnas):
        columna.append(int(input(f'introduce un elemento a la fila numero {i + 1}\n')))
    matrix.append(columna)

print('\nImprimiento la matris dinamicamente recorriendo las listas internas')
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f'[{matrix[i][j]}]' , end = "")
    print()
print('Fin')