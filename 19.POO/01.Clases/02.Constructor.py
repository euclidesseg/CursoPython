'''
En python un metodo constructor es el encargado de inicializar el estado de nuestra aplicacion,
el estado de la aplicacion correponde al valor que tendran las propiedades del programa en un determinado momento


en python un metodo constructor crea e inicializa los atributos de una clase para ser usadas por un objeto,
tambien puede sobreescribir atributos que esten definidos dentro de la clase
se define mediante el metodo __init__
'''

class Servivo():
    tipo = ""
    dieta = ""
    area = ""
    
    # Como nos dimos cuenta en este ejemplo estoy usando el metodo contructor para cambiar el estado de los atributos
    # y para crear e inicializar el nombre del ser vivo
    def __init__(self, nombre, tipo, dieta, area):
        self.tipo = tipo
        self.nombre = nombre
        self.dieta = dieta
        self.area = area        
        
    def get(self):
        return "El nombre es " + self.nombre + "\nel tipo es " + self.tipo + "\nla dieta es " + self.dieta + "\nel area es  " + self.area
                
        
servivo = Servivo("alchon", "ave", "roedores", "aire")
print(servivo.get())