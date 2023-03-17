# SE PIDE DESARROLLAR UN PROGRAMA QUE PERMITA ELIMINAR UNA PALABRA DE UNA FRACE INGRESADA POR TECLADO

# PPARA ESTE METODO USAREMOS EL METODO STRIP() USADO PARA  ELIMINAR CARATERES ESPECIFICADOS DE UNA CADENA DE CARACTERES

string = input('Por favor ingresa la frase \n')
print(string)

palabra = input('Por favor ingresa la palabra que deseas eliminar \n')

indice = string.find(palabra) 
# OBTIENE EL INDICE 0 DE DONDE EMPIEZA LA PALABRA

substring = string[0 : indice] + string[indice + len(palabra) + 1 : ]
# me crea una cadena a partir del indice 0 hasta el indice de la frace qeu se eligio para eliminar
# luego lo concatena con el string pero desde el final de la ultima letra de la palabra hasta el final de la cadena ingresada

print(substring.strip())
