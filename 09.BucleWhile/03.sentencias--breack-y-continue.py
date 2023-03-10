# EN PYTHON LOS BUCLES DE CODIGO PUEDEN SER INTERRUMPIDOS O SIMPEMENTE DEJAR DE USAR ESE CODIGO
# PARA EJECUTAR UNA NUEVA ITERACION PARA LO QUE TENEMOS BREAK Y CONTINUE

# BREAK   : SE USA PARA DETENER LA EJECUCION DE UNA ITERACION Y SALIR DE ELLA
    
contador = 0;
print('Break')
while (contador < 10):
    contador += 1
    if(contador == 5):
        print(f'hemos encontrado el numero {contador} por esta razon se detendra la ejecucion')
        break

    print(f'valor actual {contador}')
print('fin')
    


# CONTINUE : PERMITE DETENER LA ITERACION ACTUAL Y VOLVER AL PRINCIPIO DEL BUQUE
contador2 = 0
print('\nContinue')
while (contador2 < 100):
        contador2 += 10;
        if(contador2 == 50):
            continue
        #CUANDO ENCUENTRE EL VALOR DE 50 VOLVERA A EJECUTAR EL WGILE PERO NO ENTONCTRARA EL VALOR DE 50
        print(f'{contador2}')

print('fin')