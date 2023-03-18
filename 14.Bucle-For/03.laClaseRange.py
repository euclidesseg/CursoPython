# EN PYTHON LA CLASE RANGE GENERAL SECUENCIAS DE NUMEROS INMUTABLES, ES DECIR, QUE NO SE PUEDEN MODIFICAR
# ESTAS SECUENCIAS SE GENERAN A PARTIR DE UN RANGO PREVIAMENTE ESTABLECIDO

# SE UTILIZA COMO OBJETO ITERABLE DENTRO DE LA SINTAXIS DEL BUCLE O SICLO FOR CON EL CUAL SE 
# LOGRAN REALIZAR LAS RESPCTIVAS ITERACIONES 
# ESTA CLASE NOS PERMITE TRABAJAR CON MINIMO UN Y MAXIMO 3 ARGUMENTOS SIMULTANEAMENTE
# DE ESTA MANERA PODEMOS DECIDIR EL NUMERO CON EL QUE COMENZARA LA SECUENCIA DE NUMEROS Y 
# A SU VEZ INDICAR EL INCREMENTO O DECREMENTO

#SINTAXIS range(start, stop, step)

# start: es un numero que indica el numero a partir del cual se va a generar la secuencia y sismpre hara parte de la secuencia
# stop:  es un numero que indica el numero hasta el cual se va a generar la secuencia de numeros jamas sera parte de la secuencia
# step:  indica el incremento o decremento de la sucesion entre los numeros

'''
Nota: Cuando se pone solo un argumento este representa al stop
Nota: Tambien cuando solo tiene un unico argumento va a generar desde 0 y de 1 en 1
'''

# Ejemplo con un solo argumento
# En este caso va a empezar desde el numer 0 e incrementara en 1 hasta llegar a 10
range(10)


# Ejemplo con dos argumentos
# para este caso comenzara desde el numero 5 e incrementa en 1
range(5, 10)

# Ejemplo con tres argumentos
# Para este caso empezara desde 5 hasta el numero 10 e incrementara en 2 cada numero
range(0, 10, 2)

# Ejemplo con decremento
# de esta manera el  ya se sabe que el numero 10 el cual es el numero de inicio en vez de ir incrementando
# va a ir decrementando hasta llegar hasta a 0 
'''
Nota si se le da 2 argumento y el segundo es 0 no hara absolutamente nada
'''
range(10, 0, -1)