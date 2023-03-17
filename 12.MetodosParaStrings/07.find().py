# El método find() es un método de cadena en Python que se utiliza para buscar la primera 
# aparición de una subcadena en una cadena de texto. Si la subcadena se encuentra, 
# el método devuelve el índice de la posición donde comienza la subcadena en la cadena
# original. Si la subcadena no se encuentra, el método devuelve -1

cadena = "¡Hola mundo!"
subcadena = "mundo"
posicion = cadena.find(subcadena)
print(posicion) # 6

# traigamos la cadena encontrada en el string

if(posicion != -1):
    cadena_encontrada = cadena[posicion : posicion + len(subcadena)]
    print(cadena_encontrada) # mundo
else: print('La cadena no se encontro')