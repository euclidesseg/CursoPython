# IMPRIMIR LA TABLA DE MULTIPLICAR DESDE EL 1 HASTA EL 10
# INGRESANDO POR TECLADO LA TABLA QUE DESEA TENER EL RESULTADO

tabla = int(input('Por favor ingrese la tabla que desea multiplicar \n'))

print(f'La tabla del {tabla} \n')
for val in range(10 + 1):
    print(f'{ tabla } x { val } = { tabla * val }')
print('\n Fin')

