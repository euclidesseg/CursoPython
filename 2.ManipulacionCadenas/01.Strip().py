# EL METODO STRIP SE UTILIZA PARA ELIMINAR CARACTERES ESPECIFICADOS AL INICIO Y AL FINAL DE UNA CADENA
# SI NO SE LE INDICA CARACTERES SOLO ELIMINARA ESPACIOS EN BLANCO
# VEAMOS UN EJEMPLO
cadena = 'Hola vamos a usar el metodo strep...'

print(f'{len(cadena)}')

cadena1 = cadena.strip('...')

print(f'{len(cadena1)}')

print(f'{cadena1}')
