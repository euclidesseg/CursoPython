# -*- coding: utf-8 -*-

class Calculadora:
    def __init__(self, numero):
        self.n = numero
        self.datos = [0 for i in range(numero)] # creo la lista con el tamaño determinado por lo que me ingrese el usuario

    def ingresarDatos(self):
        # Este método permite ingresar datos en la lista "datos" de la clase.
        self.datos = [int(input('Ingresar Datoss' + str(i+1) + '=' )) for i in range(self.n)]



# datos = [0 for i in range(numero)] es una sintaxis de comprensión de lista en Python.
# Básicamente, crea una lista llamada "datos" con un tamaño determinado por el valor de la variable "numero".
# range(numero) crea un rango de números desde 0 hasta (numero - 1). 
# Por ejemplo, si numero es 5, el rango sería [0, 1, 2, 3, 4].
# La sintaxis [0 for i in range(numero)] crea una lista nueva, 
# donde cada elemento se inicializa con el valor 0.
# La variable "i" en este caso es solo una variable temporal 
# utilizada en la comprensión de lista. No se utiliza en este caso, 
# ya que solo necesitamos el valor de "numero" para determinar la longitud de la lista 
# y establecer todos los elementos en 0.

# EL METODO INGRESAR DATOS
# En cada iteración, se muestra un mensaje solicitando al usuario que ingrese un dato.
# El número del dato se muestra utilizando el valor de "i+1".
# El dato ingresado por el usuario se convierte a un entero utilizando la función "int()".
# El dato ingresado se asigna al elemento correspondiente en la lista "datos".
# Al finalizar el bucle, la lista "datos" contendrá los valores ingresados por el usuario.

