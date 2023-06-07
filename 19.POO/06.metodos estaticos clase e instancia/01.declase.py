"""
    En python exissten 3 tipos de metodos:
    De clase:      le pertenecen unicamente a las clases, no se pueden usar con instancias
    Estaticos:     le pertenecen tanto a la clase como a las intancias
    De instancias: le pertenecen a las instancias 
    
"""

"""
    Al crear los metodos de clase se debe anteponer la palabra o decorador @clasmethod
    al ser de las clases puedo ser llamado sin crear una instancia de la clase, es decir sin usar el __init__
    
"""

class Pastel:
    def __init__(self, ingredientes):
        self.ingredientes = ingredientes
        
    def __repr__(self):
        return f'pastel:{self.ingredientes}'
    
    
    @classmethod
    def pastel_chocolate(cls):#crea y devuelve mediante cls una intancia de Pastel
        return cls(['harina', 'leche','chocolate'])
    
    @classmethod
    def pastel_vainilla(cls):#crea y devuelve mediante cls una intancia de Pastel
        return cls(['harina', 'vainilla','leche'])
    
print(Pastel.pastel_chocolate())
print(Pastel.pastel_vainilla())


"""
    __repr__() en Python es una función especial que se utiliza 
    representar la informacion de una intancia(Objeto) de clase de forma legible.
    
    La instancia llama implícitamente al método __repr__() de la clase 
    Pastel para obtener una representación en cadena.
    
    La razón por la que se imprime con el formato de repr es debido a que el método
    __repr__() es llamado automáticamente cuando se imprime una instancia de la clase 
"""