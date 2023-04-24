'''
En python la encapsulacion de atributos se refiere a privatizar las variables de una clase 
de modo que solo puedan ser accedida por metodos accesores de la misma clase
la sintaxis para encapsular un atributo en python es la siguiente
__atributo
'''

class Servivo():
    # propiedades
    # metodos
    # este metodo sobrescribe las propiedades que ya estan
    def __init__(self):        
        self.__nombre = None
        self.__dieta = None
        self.__area = None        
        self.__tipo = None
    # declarando metodos accesores

    # property indica que este datos va a ser uns propiedad encapsulada y que sera de retorno
    @property
    def nombre(self):
        return self.__nombre
    @property
    def dieta(self):
        return self.__dieta
    @property
    def area(self):
        return self.__area
    @property
    def tipo(self):
        return self.__tipo
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    @dieta.setter
    def dieta(self, dieta):
        self.__dieta = dieta
    @area.setter
    def area(self, area):
        self.__area = area
    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo
        
        
servivo = Servivo()
servivo.nombre = "Alcon"
servivo.dieta = "aves"
servivo.area = "aire"
servivo.tipo = "ave"
print(servivo.nombre)
print(servivo.dieta)
print(servivo.tipo)
print(servivo.area)

    # por convencion de python los metodos setter y getter se suelen nombrear con el mismo 
    # nombre de la propiedad
    # y para el caso del set se le agrega el decorador property para indicar que va a retornar un valor 
    # y para el setter el mismo nombre pero con el decorador de @nombredepropiedad.setter
    