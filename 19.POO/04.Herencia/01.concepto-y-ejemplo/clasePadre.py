# Es una forma de reutilizar de código en la que se crea una nueva clase que hereda los 
# atributos y métodos de una clase existente, a la que se llama clase base o clase padre.
# La nueva clase se conoce como clase derivada o clase hija. 

class Pokemon:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        
    def descripcion(self):
        return '{} es un pokemon de tipo {}'.format(self.nombre, self.tipo)