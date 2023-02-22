
# ASIGNATION OF STRINGS CHARACTERS

mensaje = "Hola";
mensaje +=  " ";
mensaje +=  " Euclides";

print (f"{mensaje}");

print("");

# CONCATENATION OF STRING CHARACTER

mensaje = "Hola";
espacio = " ";
nombre = "Euclides";
print (f"{mensaje}{espacio}{nombre}");


# CONCATENATION OF VARIABLE WHEN IS A TYPE NUMBER

numeroUno = 4
numeroDos = 5
resultado = str(numeroUno + numeroDos);
print(f"el resultado de la sumas es {resultado}");
# ESTE CODIGO ME DA ERROR POR INTENTAR CONCATENAR UN RESULTADO
# NUMERICO CON UNA DADENA SE CORRIGE CON EL COMANDO STR PARA UNA VARIABLE DE NUMERICA A STRING


# AHORA VEAMOS UNA FOMA PARA (BUSCAR) ENTRE UNA CADENA DE CARACTERES
# EL SIGUIENTE METODO FIND ME PERMITE HALLAR LA POSISION O APARTIR DE QUE POSISION SE ENCUENTRA UNA CADENA
print('Busqueda:')
cadena = 'Hola Euclides que gusto que estes aprendiendo python'
resultadoBusqueda = cadena.find('Euclides');
print(f'{resultadoBusqueda}\n');

# AHORA VEAMOS COMO EXTRAER UNA CADENA CADENA DE TEXTO A PARTIR DE OTRA
print('Extrallendo');
resultado = cadena[5:13]
print(f'{resultado}\n');

# VEAMOS TAMBIEN LA COMPARACION 
print('Comparando');
mensajeUno = 'Hola';
mensajeDos = 'Hola';
print(mensajeUno == mensajeDos);
