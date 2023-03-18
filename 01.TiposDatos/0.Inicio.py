
# Como ya sabemos python es un lenguaje de tipado dinamico por lo que no tenemos que especificarle el tipo de 
# Datos que estamos asignano a una nueva variable unicamente agregamos el valor que queramos y python 
# asignara automaticamente en tiepo de ejecucion el tipo de dato de esa variable


# Tipo de dato entero
numero = 15;
# para saber el tipo de dato tiene un numero simplemente usamos el metodo type
print(f'{numero} {type(numero)} \n')


# Tipo de datos flotante
numeroFlotante = 15.5;
print(f'{numeroFlotante} {type(numeroFlotante)} \n')


# Tipo de datos Numero complejo
'''
 Los numeros complejos se identifican por tener una parte real y una parte imaginaria siendo esta ultima
 representada por cualquier numero y la letra j sy tipo de datos es complex
 son usados para el desarrollo e investigacion de sincias
'''
numeroComplejo = 5 + 6j
print(f'{numeroComplejo} {type(numeroComplejo)}')
print(f'{numeroComplejo.real}');
print(f'{numeroComplejo.imag} \n');

# tipo de datos string
nombre = 'Euclides'
print(f'{nombre} {type(nombre)} \n');


# Tipo de datos Bolleano
verdaderoFalso = 3 == 3;
print(f'{verdaderoFalso} {type(verdaderoFalso)}');


#NOTA PARA REDONDEAR UN DECIMAL A SOLO DOS DECIMALES HACEMOS ESTO
resultado = 7 / 3
resultado_redondeado = round(resultado, 2)