# EN ESTE CAPITULO APRENDEREMOS A SUMAR LOS ELEMENTOS DE UNA LISTA NUMERIOCA
# SU SINTAXIS ES LA SIGUIENTE:

'''
sum(objeto_iterable)   // Esta sera la lista
sum(objeto_iterable, inicio)   // Esta sera la lista y un valor numerico que se sumara al resulatado de la suma de 
los elementos del iterable
si la lista tiene un valor true se le sumara 1 al resultado de la suma ya que true tiene un valor numerico que es 1
'''

# Lista numerica
numeros = [1,2,3,4,5]
print(f'\n Lista numerica \n {numeros}')

resultado = sum(numeros, -3)
print(f'\n Resultado de la suma de los valores de la lista \n {resultado}')


# Hacer la suma con la clase range

suma = 0
for i in range(len(numeros)):
    suma = suma + numeros[i]
print(f'\n Impersion de la suma con la clase range \n {suma}')