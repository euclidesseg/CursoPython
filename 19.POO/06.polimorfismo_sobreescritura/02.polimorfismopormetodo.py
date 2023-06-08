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

for animal in (dog, cat, cow):
    print(animal.sound())
# Salida: "Woof!
# Salida: "Meow!
# Salida: "Moo!"