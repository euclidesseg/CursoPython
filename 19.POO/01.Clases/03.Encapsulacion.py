'''
En python la encapsulacion de atributos se refiere a privatizar las variables de una clase 
de modo que solo puedan ser accedida por metodos accesores de la misma clase
la sintaxis para encapsular un atributo en python es la siguiente
__atributo
'''

class Servivo():
    # propiedades
    tipo = ""
    dieta = ""
    area = ""
    
    # metodos
    # este metodo sobrescribe las propiedades que ya estan
    def __init__(self, nombre, tipo, dieta, area):
        self.__tipo = tipo
        self.__nombre = nombre
        self.__dieta = dieta
        self.__area = area        
    
    # declarando metodos accesores

    # property indica que este datos va a ser uns propiedad encapsulada y que sera de retorno
    @property
    def getNombre(self):
        return self.__nombre
    
    def getNombre(self, ):
        self.__nombre = 
        
servivo = Servivo("alchon", "ave", "roedores", "aire")
print(servivo.tipo)
print(servivo.get())