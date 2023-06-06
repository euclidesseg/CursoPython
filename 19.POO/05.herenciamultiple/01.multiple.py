#Herencia Multiple
class Telefono:
    def __init__(self):
        
        pass
    def llamar(self):
        print('llamando...')
    
    def ocupado(self):
        print('ocupado...')
        

class Camara:
    def __init__(self):
        pass
    
    def tomarFoto(self):
        print('tomando foto....')
        
        
class Reproductor():
    def __init__(self):
        pass
    
    def reproduccion(self):
        print('reproducioendo...')
        
    def reproduccionVideo(self):
        print('reproducioendo video...')
        
        
# la siguiente clase al ser un smartfone tomara las funciones de un telefono 
# y obtendra asi la referencia a las demas clases dando paso a la erencia multiple

class Smartfone(Telefono, Camara, Reproductor): 
# hasta este punto nuestra clase Smartfone ya le pertenecen todos los metodos de sus clases padres incluyecndo __init__
    
    def __del__(self):
    # este metodo es un metodo especial para limpiar los recursos
    # en python los objetos y clases se eliminan de la memoria cuando ya no se usan
        print('telefono apagado')
    
    
    
movil = Smartfone()
print(dir(movil)) # para saber que metodos especiales puedo usar con el objeto
    
movil.llamar()
movil.ocupado()
movil.tomarFoto()
movil.reproduccion()
movil.reproduccionVideo()

del(movil) #elimino el objeto para liberar la memoria ya que  no lo usare mas

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    