from clasePadre import Pokemon

#de esta forma se usa la herencia en python agregandole la clase que heredaremos dentro de los parentecis de la clase
class Pikachu(Pokemon):
    
   def ataque(self, tipoataque):
       return ' {} tipo de ataque {} '.format(self.nombre, tipoataque)
    
 
    
# Cuando una subclase Python no tiene un constructor definido,
# como en el caso de Pikachu y Charmander, Python automáticamente llama al constructor
# de la clase base Pokemon y le pasa los argumentos que recibe al crear una instancia de la subclase.
# En este caso, la clase base Pokemon tiene un constructor definido que inicializa los atributos nombre y tipo.

#  