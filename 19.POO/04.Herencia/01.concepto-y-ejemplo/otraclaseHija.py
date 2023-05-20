from clasePadre import Pokemon

class Charmander(Pokemon):
    
    def ataque(self, tipoataque):
        return ' {} tipo de ataque {} '.format(self.nombre, tipoataque)
     
  