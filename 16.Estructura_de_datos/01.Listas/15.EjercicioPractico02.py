# DESARROLLAR UN PROGRAMA QUE DADA UNA LISTA DE STRINGS LE SOLICITE AL USUARIO ITRODUCIR 
# DESDE TECLADO EL ELEMENTO QUE DESEE ELIMINAR SIN IMPORTAR QUE SEAN MAYUSCULAS O MINUSCULAS

lista = ['A', 'B', 'b', 'c', 'E', 'E', 'f']
print(lista)
eleccion = input('Por favor infgrese el dato que desee eliminar \n')

for caracter in lista: 
    if(eleccion.lower() in lista):        
        lista.remove(eleccion.lower())
    elif(eleccion.upper() in lista):
        lista.remove(eleccion.upper())
print(lista)

