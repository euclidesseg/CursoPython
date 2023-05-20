class Operacion:
    def __init__(self, n1, n2):
        self.suma = n1 + n2
        self.resta = n1 - n2
        self.multiplicacion = n1 * n2
        self.divicion = n1 / n2
        self.potencia = n1 ** n2
        self.modulo = n1 % n2
        

operacion = Operacion(280, 22);

print(operacion.suma)
print(operacion.resta)
print(operacion.multiplicacion)
print(operacion.divicion)
print(operacion.potencia)
print(operacion.modulo)

# Devido a que no tenemos una metodo en la clase que nos retorne los atributos de la clase
# Los obtenemos direactamente desde la instancia de la clase es decir, el objeto atravez de la 
# sintaxis de punto solo porque los atributos son publicos

