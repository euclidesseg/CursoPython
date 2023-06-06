# -*- coding: utf-8 -*-

class Calculadora:
    def __init__(self, numero):
        self.n = numero
        self.datos = [0 for i in range(numero)] # creo la lista con el tamaño determinado por lo que me ingrese el usuario

    def ingresarDatos(self):
        # Este método permite ingresar datos en la lista "datos" de la clase.
        self.datos = [int(input('Ingresar Dato' + str(i+1) + '=' )) for i in range(self.n)]
        # ingresare datos tantas veces como el numero que venga en el constructor



class op_basicas(Calculadora): # esta clase heredaria todos los metodos de Calculadora
    def __init__(self):
        Calculadora.__init__(self, 2) # llamo al metodo constructor  de la clase padre y le mando como parametro 2 
                                      # indicando que de ese tamañpo sera el arreglo 

    def sumar(self):
        a,b, = self.datos  # accedp al atributo datos de la clase hija que esta heredado de la clase Calculadora
        s = a + b
        print('el resultado es: ', s)

    def restar(self):
        a,b, = self.datos  # accedp al atributo datos de la clase hija que esta heredado de la clase Calculadora
        r = a - b
        print('el resultado es: ', r)

    def multiplicar(self):
        a,b, = self.datos  # accedp al atributo datos de la clase hija que esta heredado de la clase Calculadora
        m = a + b
        print('el resultado es: ', m)

    def dividir(self):
        a,b, = self.datos  # accedp al atributo datos de la clase hija que esta heredado de la clase Calculadora
        d = a + b
        print('el resultado es: ', d)
        
# Explicacion:
# Dentro de la línea a, b = self.datos, se está realizando una operación llamada "desempaquetado" o "asignación múltiple". 
# En este caso, el arreglo self.datos tiene dos elementos y se espera que se asignen a las variables a y b en orden.
# se debe poner coma despues de cada elemento que vallamos a usar para desempaquetar el arreglo

class raiz(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,1) # llamo al metodo de la clase padre y le mando como parametro 2

    
    def raizCuadrada(self):
        import math
        a, = self.datos # debido a que el metodo
        raiz = math.sqrt(a)
        print(f'la raiz cuadrada de {1} es {raiz}')
        
    def raizCuvida(self):
        import math
        a, = self.datos
        raizCuvica = math.pow(a, 1/3)
        print(f'la raiz cuvica de {a} es {raizCuvica}')

ejemplo = op_basicas()
ejemplo.ingresarDatos()
ejemplo.sumar()

# funciones de prueba 
print(isinstance(ejemplo, op_basicas)) # me retorna verdadero porque esta clase si es una intancia
print(isinstance(ejemplo, raiz)) # me retorna falso porque esta clase no trabaja con la clase raiz


ejemplo2 = raiz()
ejemplo2.ingresarDatos()
ejemplo2.raizCuvida()