'''
Creando una clase Coche
'''
class Coche():
    #propiedades
    largoChasis = 250
    ancho = 120
    enMarcha = False
    color = "azul"

    #comportamientos
    '''
    La palabra self en este metodo indica que se va a recibir por parametro el mismo objeto que se declare para poder usar
    y acceder a las propiedades de la clase 
    '''
    def acelerar(self, aceleracion):
        aceleracion = aceleracion
        self.enMarcha = True
        print(f'El coche ha acelerado {aceleracion} km')
        
    def estado(self):
        print(f'el largo del coche es {self.largoChasis}')
        print(f'el ancho del coche es {self.ancho}')
        print(f'el color del coche es {self.color}')
        
coche1 = Coche()

print(f'el coche esta en marcha? {coche1.enMarcha}')
coche1.acelerar(25)
print(f'el coche esta en marcha? {coche1.enMarcha}')



print("========= Creamos nuestro segundo objeto =============")
coche2 = Coche()
coche1.estado()
