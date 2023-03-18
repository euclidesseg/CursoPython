# INGRESAR UNA FRASE DESDE TECLADO E IMPRIMIR ESA FRASE SIN VOCALES TAMBIEN SE SEBE INGRESAR UN CARACTER EN ESPESIFICO
# Y SI EL CARACTER ESPECIFICO ES PARTE DE LA FRACE EL BUCLE DEBE TERMINAR SU EJECUCION

frase = input('Por favor ingrese la frase para evaluar \n')
letter = input('Por favor ingrese el caracter especial \n')

for character in frase:
    if(character.lower() == letter.lower()):
        break
    elif(character.lower() == 'a'):
        continue
    elif(character.lower() == 'e'): 
        continue
    elif(character.lower() == 'i'):
        continue
    elif(character.lower() == 'o'):
        continue
    elif(character.lower() == 'u'):
        continue
    print(character, end = "") # con end = "" hago que no me de saltos de lineas cada impresion en pantalla
    
print('\n Fin')