# Tambien podemos crear una lista de acuerdo a una condicion 
# dentro de nuestra expresion de lista de compresion y se hace de la siguiente manera tomaremos como 
# ejemplo el ejersicio pasado

listaNumeros = [num for num in range(0,100) if num % 2 == 0]
print(listaNumeros)

# En este caso se van a agregar solo los numeros que sean pares a nuestra lista de numeros