# En esta ocacion crearemos una clase persona y tomaremos como ejempo la funcion format
# El mÃ©todo format() en Python se utiliza para formatear cadenas de caracteres.

class Persona:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.año = edad
        
    def descripcion(self):
        return '{} tiene {}'.format(self.nombre, self.edad)
    
    
#  formato es ' {} tiene {}', donde las llaves {} indican las posiciones donde se insertaran los valores correspondientes que se desea mostrar.

    def comentario(self, frase):
        return '{} dice {}'.format(self.nombre, frase)


#CREAMOS OBJETO PARA LA CLASE PERSONA

doctor = Persona('Euclides',26)
print(doctor.descripcion())
print(doctor.comentario('Hola soy programador'))
