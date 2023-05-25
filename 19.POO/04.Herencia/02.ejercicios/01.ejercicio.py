# -*- coding: utf-8 -*-

class Calculadora:
    def __init__(self, numero):
        self.n = numero
        self.datos = [0 for i in range(numero)] # creo la lista con el tamaño determinado por lo que me ingrese el usuario

    def ingresarDatos(self):
        # Este método permite ingresar datos en la lista "datos" de la clase.
        self.datos = [int(input('Ingresar Dato' + str(i+1) + '=' )) for i in range(self.n)]
        # ingresare datos tantas veces como el numero que venga en el constructor



class op_basicas(Calculadora):
    def __init__(self):
        Calculadora.__init__(self, 2)

        def sumar(self valor1, valor2):
           a,b, = self.datos
           s = a + b
           print('el resultado es: ', s)

           def restar(self valor1, valor2):
           a,b, = self.datos
           r = a - b
           print('el resultado es: ', r)

           def multiplicar(self valor1, valor2):
           a,b, = self.datos
           m = a + b
           print('el resultado es: ', m)

           def dividir(self valor1, valor2):
           a,b, = self.datos
           d = a + b
           print('el resultado es: ', d)

class raiz(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,1)

    
    def