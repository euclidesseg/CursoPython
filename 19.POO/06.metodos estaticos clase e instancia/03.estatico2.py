class MiClase:
    atributo_estatico = 0

    def __init__(self):
        self.atributo_no_estatico = 0

    @staticmethod
    def metodo_estatico():
        print("Método estático")


ob1 = MiClase()
ob2 = MiClase()

MiClase.atributo_estatico = 10
print(ob1.atributo_estatico)
print(ob2.atributo_estatico)
