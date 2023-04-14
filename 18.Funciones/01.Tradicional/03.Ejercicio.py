# Esriba un programa que pida el anchi y el alto de un rectangulo
# y permita calcular su area perimetro graficar el rectangulo

largo = int(input("Por favor ingrese el largo del rectangulo"))
ancho = int(input("Por favor ingrese el ancho del rectangulo"))

def calcularArea(largo,ancho):
    return ancho * largo

def calcularPerimetro(largo,ancho):
    return 2*(largo + ancho)

print(f"Area: {calcularArea(largo, ancho)}")
print(f"Perimetro: {calcularPerimetro(largo, ancho)}")

for la in range(largo):
    for an in range(ancho):
        print("*" , end = "")
    print()
print('Fin')