# LAS MATRICES SON UNA ESTRUCTURA DE DATOS BIDIMENSIONAL ES DECIR TIENE FILAS Y COLUMNAS QUE CONFORMAN SUS DATOS
# UNA FORMA DE GENERAR MATRICES ES CREANDO LISTAS ANIDADAS

'''
veamos su implementacion

'''

matrix = [ [1,2,3], [4,5,6], [7,8,9] ]

print('\nImprimiendo la matris con un siclo for simple')
for fila in matrix:
    print(fila)
    
print('\nImprimiento la matris dinamicamente recorriendo las listas interna')
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f'[{matrix[i][j]}]' , end = "")
    print()
print('Fin')