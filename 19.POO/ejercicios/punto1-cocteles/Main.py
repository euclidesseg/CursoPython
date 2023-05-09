from Coctel import Coctel
class Main:

    print('* ******************* *')
    print('*                     *')
    print('* COCTELES LE FRONENT *')
    print('*                     *')
    print('* ******************* *\n')

    shot  = Coctel()

    respuesta = input('¿Deseas realizar una orden? ingrese SI o No')
    def calcularCoctelFrutas(unidades, valor, añejamiento):
        if añejamiento <= 1:
            return unidades * valor
        elif añejamiento == 2:
            return (unidades * valor) - ((unidades * valor) * 0.2)
        elif añejamiento == 3:
            return (unidades * valor) - ((unidades * valor) * 0.5)
        else:
            return "Lo siento no se puede vender un coctel con añejamiento mayor a 3"
    
    while respuesta.lower() == "si":
        print('*******************************')
        print('Tenemos las siguientes opciones')

        print("Selecciona 1 para Shot(cocteles con alcohol) $ 15000")
        print("Selecciona 2 para Frutas(cocteles con Frutas) $ 16000")
        opcion = int(input("Por favor escoje una opcion:  "))

        if opcion == 1:
            
            fruta = Coctel()
            fruta.nombre = input("por favor ingrese el nombre del coctel:  ")
            fruta.grados = input("por favor ingrese los grados de alchool:  ")
            fruta.precio = 15000
            fruta.cantidad = int (input("Ingrese la cantidad que desea:"))
            resultado = fruta.precio * fruta.cantidad
            print(f"por favor espere! su orden tiene un valor de ${resultado} pesos")

        elif opcion == 2:
            shot = Coctel()
            shot.nombre = input("por favor ingrese el nombre del coctel:  ")
            shot.precio = 15000
            shot.cantidad = int (input("Ingrese la cantidad que desea:"))
            añejamiento = int(input("por favor ingrese el añejamiento del coctel:  "))

            respuesta = calcularCoctelFrutas(shot.cantidad, shot.precio, añejamiento)
            print(respuesta)

           
        respuesta = input('¿Deseas realizar otra orden?')
    print("Gracias por su interes")
