"""
    Polimorfismo en python es la capacidad que tienen los objetos 
    para comportarse de una forma diferente dependiendo de la situacion que se presente

    El polimorfismo se refiere a la capacidad de objetos de diferentes clases 
    de responder al mismo método de manera diferente. En este caso, las clases

"""
class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

class Cow(Animal):
    def sound(self):
        return "Moo!"

# Creamos objetos de diferentes clases y llamamos al método sound
dog = Dog()
cat = Cat()
cow = Cow()

print(dog.sound())  # Salida: "Woof!"
print(cat.sound())  # Salida: "Meow!"
print(cow.sound())  # Salida: "Moo!"


"""
    Podemos ver que en este ejemplo vemos POLIMORFISMO aplicado al ver que 
    cada objeto de cada clase hace la implementacion diferente del metodo sound de la clase padre

    Podemos ver sobreescritura aplicada cuando observamos que cada clase hace una implemetacion 
    diferente del metodo sound() sobreescribiendo asi el contenido original
"""
