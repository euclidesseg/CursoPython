# INVERTIR UNA CADENA DE CARATERES INGRESADA POR EL USUARIO

cadena = input('Ingresa la cadena a invertir \n')
string_reversed = ''
for letra in cadena:
    string_reversed = letra + string_reversed
print(string_reversed)