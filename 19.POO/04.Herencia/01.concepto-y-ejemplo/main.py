from claseHIja import Pikachu
from otraclaseHija import Charmander

class Main:
    nuevo_pokemon = Pikachu('boby', 'agua')
    print(nuevo_pokemon.descripcion())
    
    # En python al instanciar un objeto de una clase que esta heredando de una superclase,
    # le puedo mandar los datos a la superclase directamente desde el contructor de la case hija y eso se pasara automaticamente
    
    nuevo_pokemon2 = Charmander('karra', 'aire')
    print(nuevo_pokemon2.descripcion())
