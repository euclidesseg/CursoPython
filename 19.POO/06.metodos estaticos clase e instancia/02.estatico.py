"""
        Metodos estaticos representados mediante @staticmethod
        estos metodos pueden ser llamados sin tener una instancia de la clase
        asi como tambien pueden ser llamados mediante una instancia
        
        es por eso que se conocen por no pertenecer ni a instancias ni a clases
        
        
"""
import math
class Pastel:
    def __init__(self, ingredientes, tamaño):
        self.ingredientes = ingredientes
        self.tamaño = tamaño
        
    
    def __repr__(self):
        return f'pastel:{self.ingredientes}, {self.tamaño}'
    
    def area(self):
        return self.tamaño_area(self.tamaño)
    
    @staticmethod
    def tamaño_area(a):
        return a ** 2 * math.pi
    
pastel = Pastel(['arina','leche','vainilla'], 25)
print(pastel.area())
